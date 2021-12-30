from copy import copy
from Piece import Piece

BOARD_SIZE = 20
SEPARATOR_LEN = 30


class TetrisBoard:
    def __init__(self):
        self.board = ["*" + " " * BOARD_SIZE + "*" for _ in range(BOARD_SIZE)]
        self.board.append("*" + "*" * BOARD_SIZE + "*")

    def redraw_board(self):
        print("\n" + "-" * SEPARATOR_LEN + "\n")
        for line in self.board:
            print(line)

    def place_piece_on_board(self, pce):
        shape = Piece.SHAPES[pce.shape][pce.rotate_pos]
        for y in range(len(shape)):
            for x in range(len(shape[0])):
                if shape[y][x] == "*":
                    # insert star at the respective position on the respective line
                    self.board[pce.Y + y] = self.board[pce.Y + y][:pce.X + x]\
                                            + "*"\
                                            + self.board[pce.Y + y][pce.X + x + 1:]

    def remove_piece_from_board(self, pce):
        shape = Piece.SHAPES[pce.shape][pce.rotate_pos]
        for y in range(len(shape)):
            for x in range(len(shape[0])):
                if shape[y][x] == "*":
                    # remove star at the respective position on the respective line
                    self.board[pce.Y + y] = self.board[pce.Y + y][:pce.X + x]\
                                            + " "\
                                            + self.board[pce.Y + y][pce.X + x + 1:]

    def is_new_position_possible(self, pce):
        shape = Piece.SHAPES[pce.shape][pce.rotate_pos]
        for y in range(len(shape)):
            for x in range(len(shape[0])):
                if shape[y][x] == "*" and self.board[pce.Y + y][pce.X + x] == "*":
                    return False
        return True

    def is_move_possible(self, pce, next_move):
        pce_next_position = copy(pce)
        if next_move == "a":
            pce_next_position.move_left()
        elif next_move == "d":
            pce_next_position.move_right()
        elif next_move == "w":
            pce_next_position.rotate_counterclockwise()
        elif next_move == "s":
            pce_next_position.rotate_clockwise()
        return self.is_new_position_possible(pce_next_position)

    def is_move_piece_line_down_possible(self, pce):
        pce_line_down = copy(pce)
        pce_line_down.move_line_down()
        return self.is_new_position_possible(pce_line_down)

    def is_any_move_possible(self, pce):
        for move_to_try in ("a", "d", "w", "s"):
            if self.is_move_possible(pce, move_to_try):
                return True
        return False

    def is_new_piece_placement_possible(self, pce):
        return self.is_new_position_possible(pce)