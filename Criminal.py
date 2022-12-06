import arcade


class Criminal(arcade.Sprite):
    def __init__(self, texture):
        super().__init__()

        self.health = 1
        self.scale = 1
        self.texture = arcade.load_texture(texture)


    def follow_sprite(self, player_sprite):

        if self.center_y < player_sprite.center_y:
            self.center_y += min(1, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(1, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(1, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(1, self.center_x - player_sprite.center_x)

    def type(self, texture):
        if texture == "twoface.jpg":
            return 1
        if texture == "criminal.png":
            return 0

    def set_type(self, texture):
        if texture == "twoface.jpg":
            self.texture = texture
            return 1

        if texture == "criminal.png":
            self.texture = texture
            return 0

    def death(self, sprite):
        sprite.remove_from_sprite_lists()
