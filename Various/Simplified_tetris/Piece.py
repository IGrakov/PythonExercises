from random import randint


class Piece:
    SHAPES = {
        0: [
            [
                "*   ",
                "*   ",
                "*   ",
                "*   "
            ],
            [
                "    ",
                "    ",
                "    ",
                "****"
            ]
        ],
        1: [
            [
                "*  ",
                "*  ",
                "** "
            ],
            [
                "   ",
                "***",
                "*  "
            ],
            [
                "** ",
                " * ",
                " * "
            ],
            [
                "   ",
                "  *",
                "***"
            ]
        ],
        2: [
            [
                " * ",
                " * ",
                "** "
            ],
            [
                "   ",
                "*  ",
                "***"
            ],
            [
                "** ",
                "*  ",
                "*  "
            ],
            [
                "   ",
                "***",
                "  *"
            ]
        ],
        3: [
            [
                " * ",
                "** ",
                "*  "
            ],
            [
                "   ",
                "** ",
                " **"
            ]
        ],
        4: [
            [
                "**",
                "**",
            ]
        ]
    }

    def __init__(self):
        self.shape = randint(0, len(Piece.SHAPES) - 1)
        self.rotate_pos = 0
        shape = Piece.SHAPES[self.shape][self.rotate_pos]
        self.X = randint(1, 21 - len(shape) + self.calc_min_right_blank_spaces())
        self.Y = 0

    def rotate_clockwise(self):
        # Switch shapes in circle clockwise
        self.rotate_pos += 1
        if self.rotate_pos > len(Piece.SHAPES[self.shape]) - 1:
            self.rotate_pos = 0

    def rotate_counterclockwise(self):
        # Switch shapes in circle counterclockwise
        self.rotate_pos -= 1
        if self.rotate_pos < 0:
            self.rotate_pos = len(Piece.SHAPES[self.shape]) - 1

    def move_left(self):
        self.X -= 1

    def move_right(self):
        self.X += 1

    def move_line_down(self):
        self.Y += 1

    def calc_min_right_blank_spaces(self):
        min_spaces = 4
        for line in Piece.SHAPES[self.shape][self.rotate_pos]:
            spaces = 0
            for idx in range(len(line) - 1, 0, -1):
                if line[idx] == " ":
                    spaces += 1
                else:
                    break
            min_spaces = min(min_spaces, spaces)
        return min_spaces
