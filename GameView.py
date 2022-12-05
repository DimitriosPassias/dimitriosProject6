import arcade
import random
from Criminal import Criminal
from PauseView import PauseView
from GameOver import GameOver

MAX_SPEED = 3.0
ACCELERATION_RATE = 0.1
FRICTION = 0.03
ENEMY_SPEED = 3
MAX_PLAYER_AMMO = 5
COIN_SCALING = 0.5
TOTAL_SCORE = 0

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = None
        self.targets = arcade.SpriteList()
        self.score = 0
        self.background= None
        self.player_list = None
        self.player_ammo_list = None
        self.player_dx = 0
        self.player_dy = 0
        self.up_pressed= None
        self.down_pressed=None
        self.right_pressed=None
        self.left_pressed=None
        self.hurt_sound = None
        self.death_sound=None
        self.enemy_textures = None
        self.total_time=0.0

        self.window.set_mouse_visible(False)

        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.batarang_sound = arcade.load_sound("BatarangSound.mp3")


    def on_show_view(self):
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def setup(self):
        self.hurt_sound = arcade.load_sound("bathit.mp3")
        self.death_sound= arcade.load_sound("death.mp3")
        self.player_list = arcade.SpriteList()
        self.player_ammo_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.background = arcade.load_texture("background.jpg")
        self.player = arcade.Sprite("batman.png", 1, 106, 0, 29, 48)

        self.score = 0
        self.player.center_x = 64
        self.player.center_y = 128

        self.player_list.append(self.player)
        for number in range(6):
            criminal = arcade.Sprite("criminal.png", 1, 227, 0, 27, 32)
            self.targets.append(criminal)
            criminal.center_x = random.randint(16, 1184)
            criminal.center_y = 880



    def on_update(self, delta_time):
        self.player_list.update()
        self.player_list.update_animation()
        self.player_ammo_list.update()
        TOTAL_SCORE = self.score

        if self.player.change_x > FRICTION:
            self.player.change_x -= FRICTION
        elif self.player.change_x < -FRICTION:
            self.player.change_x += FRICTION
        else:
            self.player.change_x = 0

        if self.player.change_y > FRICTION:
            self.player.change_y -= FRICTION
        elif self.player.change_y < -FRICTION:
            self.player.change_y += FRICTION
        else:
            self.player.change_y = 0

            # Apply acceleration based on the keys pressed
        if self.up_pressed and not self.down_pressed:
            self.player.change_y += ACCELERATION_RATE
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y += -ACCELERATION_RATE
        if self.left_pressed and not self.right_pressed:
            self.player.change_x += -ACCELERATION_RATE
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x += ACCELERATION_RATE

        if self.player.change_x > MAX_SPEED:
            self.player.change_x = MAX_SPEED
        elif self.player.change_x < -MAX_SPEED:
            self.player.change_x = -MAX_SPEED
        if self.player.change_y > MAX_SPEED:
            self.player.change_y = MAX_SPEED
        elif self.player.change_y < -MAX_SPEED:
            self.player.change_y = -MAX_SPEED


        for batarang in self.player_ammo_list:
            hit_list = arcade.check_for_collision_with_list(batarang, self.targets)
            if len(hit_list) > 0:
                batarang.remove_from_sprite_lists()
                arcade.play_sound(self.hurt_sound)
            if batarang.bottom > 900:
                batarang.remove_from_sprite_lists()
            for criminal in hit_list:
                criminal.remove_from_sprite_lists()
                self.score +=1
                self.window.total_score +=1

        #sets the criminals to go towards player
        for criminal in self.targets:
            Criminal.follow_sprite(criminal, self.player)

        #sends user from top to bottom or bottom to top of the screen
        if self.player.center_y < 0:
            self.player.center_y = 900
        if self.player.center_y > 900:
            self.player.center_y = 0

        #end game if user gets coins or gets hit
        if arcade.check_for_collision_with_list(self.player, self.targets):
            arcade.play_sound(self.)
            view = GameOver()
            self.window.show_view(view)
        if self.window.total_score == 20:
            view = GameOver()
            self.window.show_view(view)

        self.total_time=delta_time

        while len(self.targets) <= 5:
            for number in range(5):
                criminal = arcade.Sprite("criminal.png", 1, 227, 0, 27, 32)
                self.targets.append(criminal)
                criminal.center_x = random.randint(16, 1184)
                criminal.center_y = 880

    def on_draw(self):
        #starts render and draws objects
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,1820, 900,self.background)
        self.player_list.draw()
        self.targets.draw()
        self.player_ammo_list.draw()

        #Draws Score
        output = f"BatPoints: {self.score}"
        arcade.draw_text(output, 10, 870, arcade.color.YELLOW)

    def on_key_press(self, key, modifiers):
        #Movement for the keys
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
        if key == arcade.key.ESCAPE:
            pause = PauseView(self)
            self.window.show_view(pause)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        if len(self.player_ammo_list) < 5:
            arcade.play_sound(self.batarang_sound)

            batarang = arcade.Sprite("batarang.png", 1, 49, 0, 15, 10)
            batarang.change_y = 3
            batarang.center_x = self.player.center_x
            batarang.bottom = self.player.top

            #Sends the batarang
            self.player_ammo_list.append(batarang)

