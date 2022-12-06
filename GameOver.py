import arcade
import GameView



class GameOver(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()

        score = self.window.total_score

        if score >= 20:
            arcade.draw_lrwh_rectangle_textured(0, 0, 1800, 900, arcade.load_texture("winningscreen.jpg"))
            arcade.draw_text("You Win", 240, 400, arcade.color.WHITE, 54)
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, 1600, 900, arcade.load_texture("losingscreen.png"))
            arcade.draw_text("You Lost", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to Restart", 310, 300, arcade.color.WHITE, 24)
        arcade.draw_text(f"Total Score: {score}", 310, 250, arcade.color.WHITE, 18)


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        game_view = GameView.GameView()
        game_view.setup()
        self.window.total_score = 0
        self.window.show_view(game_view)
