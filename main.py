import arcade
from MainMenu import MainMenu


def main():
    window = arcade.Window(1820, 900, "Batman: The Game")
    window.total_score = 0
    menu_view = MainMenu()
    window.show_view(menu_view)
    arcade.run()


main()