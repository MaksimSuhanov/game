import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Rectangle:
    def __init__(self, x, y, w, h, color, tlit=0, filled=True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.tlit = tlit
        self.filled = filled
        self.change_x = 3
    def draw(self):
        if not self.filled:
            arcade.draw_rectangle_outline(self.x, self.y, self.w, self.h, self.color)
        else:
            arcade.draw_rectangle_filled(self.x, self.y, self.w, self.h, self.color)

    def update(self):
        self.x += self.change_x
        if self.x + self.w / 2 > SCREEN_WIDTH or self.x - self.h < 0:
            self.change_x = - self.change_x

    def change_size(self):
        if self.x + self.w / 2 >= SCREEN_WIDTH or self.x - self.w / 2 <= 0:
            self.w += 2
            self.h += 2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title='Анимация' )
        self.background_color = arcade.color.SKY_BLUE
        self.rectangle1 =  Rectangle(200, 100, 40, 50, arcade. color.RED_DEVIL)

    def on_draw(self):
        self.clear()
        self.rectangle1.draw()

    def update(self, delta_time: float):
        self.rectangle1.update()
        self.rectangle1.change_size()
        self.rectangle1.draw()

if __name__ == '__main__':
    game = Game()
    arcade.run()
