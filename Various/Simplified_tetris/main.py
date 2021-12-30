from TetrisBoard import TetrisBoard
from Piece import Piece

board = TetrisBoard()
piece = Piece()


def next_move_prompt():
    return input("a (return): move piece left\n" +
                 "d (return): move piece right\n" +
                 "w (return): rotate piece counter clockwise\n" +
                 "s (return): rotate piece clockwise\n" +
                 "q (return): quit\n" +
                 ">>> ").lower()


def game_over():
    print("New piece cannot be placed. Game over")
    quit(0)


def place_new_piece():
    global piece
    board.place_piece_on_board(piece)
    piece = Piece()
    if not board.is_new_piece_placement_possible(piece):
        board.redraw_board()
        game_over()


if __name__ == "__main__":

    while True:
        board.place_piece_on_board(piece)
        board.redraw_board()
        board.remove_piece_from_board(piece)

        if not board.is_any_move_possible(piece):
            game_over()

        move = next_move_prompt()

        if move == "q":
            quit(0)
        elif move in ("a", "d", "w", "s") and board.is_move_possible(piece, move):
            if move == "a":
                piece.move_left()
            elif move == "d":
                piece.move_right()
            elif move == "w":
                piece.rotate_counterclockwise()
            elif move == "s":
                piece.rotate_clockwise()
            # Check if piece can be moved line down at current move
            if board.is_move_piece_line_down_possible(piece):
                piece.move_line_down()
            else:
                place_new_piece()
            # Check if piece can be moved line down at the next move
            if not board.is_move_piece_line_down_possible(piece):
                place_new_piece()
        else:
            print("Such move is not possible. Try again")
