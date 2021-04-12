import pyglet
from game import Game


class MyWindow(pyglet.window.Window):

    def __init__(self, width, height, *args, **kwargs):
        super().__init__(width, height, *args, *kwargs)

        # center location on screen
        display = pyglet.canvas.Display()
        screen = display.get_default_screen()
        location_x = (screen.width - height) // 2 if (screen.width - width) // 2 > 0 else 0
        location_y = (screen.height - height) // 2 if (screen.height - width) // 2 > 0 else 0
        self.set_location(location_x, location_y)

        # setting background fill color
        pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)

        # enabling opacity
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)

    def on_draw(self):
        self.clear()
        game.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        game.run(x, y)

    def on_key_press(self, symbol, modifiers):
        pass

    @classmethod
    def schedule(cls):
        pyglet.clock.schedule(cls.scheduled_function)

    @staticmethod
    def scheduled_function(dt):
        game.schedule()


if __name__ == "__main__":
    WIN_SIZE = 900
    win = MyWindow(WIN_SIZE, WIN_SIZE)

    SIZE = 4
    game = Game(win, WIN_SIZE - 100, SIZE, 50, 50)
    game.show_solution()

    MyWindow.schedule()
    pyglet.app.run()
