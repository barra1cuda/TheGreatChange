from graphics import Graphics
from random import randint


class Game:

    def __init__(self, window, g_size, size, x_off=0, y_off=0):
        self.window = window
        self.size = size
        self.x_off = x_off
        self.y_off = y_off
        self.field_size = g_size / size
        self.finished = False
        self.sleeping = False
        self.grid_vertex_list = [[None for _ in range(size)] for _ in range(size)]
        self.line_vertex_list = [None for _ in range(size + 1)]
        self.text = Graphics.text("", g_size // 2 + x_off, g_size // 2 + y_off, 30)
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.shuffle()

        # fields
        for i_row, row in enumerate(self.grid):
            for i_field, field in enumerate(row):
                color = (200, 55, 105) if field else (250, 200, 0)
                self.grid_vertex_list[i_row][i_field] = Graphics.rect(self.x_off + self.field_size * i_row,
                                                                        self.y_off + self.field_size * i_field,
                                                                        self.field_size, self.field_size,
                                                                        color=color)
        # lines
        line_width = self.field_size // 30
        for line in range(self.size + 1):
            x1 = self.x_off + self.field_size * line - line_width // 2
            y1 = self.y_off - line_width // 2
            w1 = line_width
            h1 = self.field_size * self.size + line_width
            self.line_vertex_list[line] = Graphics.rect(x1, y1, w1, h1)

            x2 = self.x_off - line_width // 2
            y2 = self.y_off + self.field_size * line - line_width // 2
            w2 = self.field_size * self.size + line_width
            h2 = line_width
            self.line_vertex_list[line] = Graphics.rect(x2, y2, w2, h2)

    @staticmethod
    def draw():
        Graphics.draw()

    def update(self, r, f):
        self.grid[r][f] = 0 if self.grid[r][f] else 1
        self.grid_vertex_list[r][f].colors = (200, 55, 105) * 4 \
            if self.grid[r][f] else (250, 200, 0) * 4

    def run(self, x, y):
        if not self.finished:
            for i_row, row in enumerate(self.grid):
                for i_field, field in enumerate(row):
                    if self.x_off + self.field_size * i_row < x <= self.x_off + self.field_size * (i_row + 1) and \
                            self.y_off + self.field_size * i_field < y <= self.y_off + self.field_size * (i_field + 1):

                        self.update(i_row, i_field)
                        self.update(i_row + 1, i_field) if not i_row + 1 > len(self.grid) - 1 else None
                        self.update(i_row, i_field + 1) if not i_field + 1 > len(self.grid) - 1 else None
                        self.update(i_row - 1, i_field) if not i_row - 1 < 0 else None
                        self.update(i_row, i_field - 1) if not i_field - 1 < 0 else None

        self.check_for_win()

    def check_for_win(self):
        won_c1, won_c2 = True, True

        for row in self.grid:
            for field in row:
                won_c1 = False if field else won_c1
                won_c2 = False if not field else won_c2
        if won_c2 or won_c1:
            self.sleeping = 1 * 60 + 1
            self.finished = True
            self.text.text = "You won!"

    def reset(self):
        self.text.text = ""
        self.grid = [[0 if (a + b) % 2 else 1 for a in range(self.size)] for b in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.update(i, j)
        self.finished = False
        self.sleeping = False

    def shuffle(self):
        for a in range(self.size):
            for b in range(self.size):
                self.grid[a][b] = randint(0, 1)
                
    def schedule(self):
        if self.sleeping > 1:
            self.sleeping -= 1
        elif self.sleeping == 1:
            self.reset()

    def show_solution(self):
        new_lines = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i, line in enumerate(self.grid):
            for j, num in enumerate(reversed(line)):
                new_lines[j][i] = num

        for i in new_lines:
            print(i)


if __name__ == "__main__":
    pass
