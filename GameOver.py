import arcade
import GameView



class GameOver(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        if (self.window.total_score) == 20:
            arcade.draw_text("You Win", 240, 400, arcade.color.WHITE, 54)
        else:
            arcade.draw_text("You Lost", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to Restart", 310, 300, arcade.color.WHITE, 24)
        arcade.draw_text(f"Total Score: {self.window.total_score}", 40, 40, arcade.color.WHITE, 24)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        game_view = GameView.GameView()
        game_view.setup()
        self.window.show_view(game_view)
