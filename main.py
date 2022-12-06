#Extra Credit: Three Lives, Two Types of Entities
#just run the main and make sure to have the textures added. You dont need all the textures as some are extra and will be added later for personal use.
#Issues: Spawning Entites over certain time point but i got certain amount of entities on screen at a time so it automatically loads another after one dies basically.
import arcade
from MainMenu import MainMenu


def main():
    #opens a window then adds views
    window = arcade.Window(1820, 900, "Batman: The Game")
    window.total_score = 0
    menu_view = MainMenu()
    window.show_view(menu_view)
    arcade.run()


main()