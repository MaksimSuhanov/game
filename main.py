import arcade

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title='Анимация')
        self.background_color = (255, 255, 255)
        self.texture = arcade.load_texture('background.jpg')
        self.x = 100
        self.y = 100
        self.radius = 30
        self.color = arcade.color.RED_DEVIL
        self.change_x = 3
        self.change_y = 3

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(center_x = 400, center_y = 300, width = 800, height = 600,texture = self.texture)
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
        for i in range(1, 4):
            create_cloud(100 * i, 400)
        for j in range(1, 3):
            create_cloud(100 * j + 50, 470)

    def setup(self):
        pass

    def update(self, delta_time: float):
        self.x += self.change_x
        self.y += self.change_y
        if self.x + self.radius / 2 > 800 or self.x - self.radius / 2 < 0:
            self.change_x = - self.change_x
        if self.y + self.radius / 2 > 600 or self.y - self.radius / 2 < 0:
            self.change_y = - self.change_y

def create_cloud(x, y):
    arcade.draw_circle_filled(center_x=x, center_y=y, color = arcade.color.WHITE, radius=60)

if __name__ == '__main__':
    game = MyGame()
    game.setup()
    arcade.run()
