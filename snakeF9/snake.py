import pygame.event

import consts


class Snake:
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        # پوزیشن جدید سر مار
        pos_of_new_head = (self.val(self.get_head()[0] + Snake.dx[self.direction]),
                           self.val(self.get_head()[1] + Snake.dy[self.direction]))
        # مختصات پوزیشن سر مار
        cell_of_new_head = self.game.get_cell(pos_of_new_head)
        if cell_of_new_head.color == consts.back_color:  # برای وقتی که خونه بعدی خالی باشه
            cell_of_new_head.set_color(self.color)
            self.cells.append(pos_of_new_head)
            self.game.get_cell(self.cells[0]).set_color(consts.back_color)
            del self.cells[0]
        elif cell_of_new_head.color == consts.fruit_color:
            cell_of_new_head.set_color(self.color)
            self.cells.append(pos_of_new_head)
        else:
            self.game.kill(self)

    def handle(self, keys):
        for key in keys:
            if key in self.keys.keys():
                if self.direction == 'LEFT' or self.direction == 'RIGHT':
                    if self.keys[key] == 'UP':
                        self.direction = 'UP'
                        break
                    elif self.keys[key] == 'DOWN':
                        self.direction = 'DOWN'
                        break
                    else:
                        pass
                elif self.direction == 'UP' or self.direction == 'DOWN':
                    if self.keys[key] == "LEFT":
                        self.direction = 'LEFT'
                        break
                    elif self.keys[key] == 'RIGHT':
                        self.direction = 'RIGHT'
                        break
                    else:
                        pass