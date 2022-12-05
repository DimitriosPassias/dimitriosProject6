import arcade
from GameView import GameView


class MainMenu(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1820, 900,arcade.load_texture("menu.jpg"))
        arcade.draw_text("Batman: The Game", 0, 450,
                         arcade.color.BLACK, 50,"center")
        arcade.draw_text("Click to advance", 0, 450 - 75,
                         arcade.color.GRAY, 20, "center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

