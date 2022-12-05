import arcade
import GameView


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view


    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE)


    def on_draw(self):
        self.clear()


        player = self.game_view.player
        player.draw()


        arcade.draw_lrtb_rectangle_filled(player.left,
                                      player.right,
                                      player.top,
                                      player.bottom,
                                      arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSED", 1820 / 2, 900 / 2 + 50,arcade.color.BLACK, 50, "center")


        arcade.draw_text("Press Esc. to return",
                     1820 / 2, 900 / 2, arcade.color.BLACK,20,"center")
        arcade.draw_text("Press Enter to reset",
                     1820 / 2, 900 / 2 - 30, arcade.color.BLACK,20,"center")


    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:  # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView.GameView()
            game.setup()
            self.window.show_view(game)
