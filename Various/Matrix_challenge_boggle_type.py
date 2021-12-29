# Write a function matrix_challenge(str_lst) read list of strings stored in str_lst,
# which will contain 2 elements: the first element will represent a 4x4 matrix of letters,
# and the second element will be a long string of comma-separated words each at least 3 letters long,
# in alphabetical order, that represents a dictionary of some arbitrary length.
# For example: str_lst can be: ["rbfg, ukop, fgub, mnry", "bog,bop,gup,fur,ruk"].
# Your goal is to determine if all the comma separated words as the second parameter
# exist in the 4x4 matrix of letters.
#
# For this example, the matrix looks like the following:
# r b f g
# u k o p
# f g u b
# m n r y
#
# The rules to make a word are as follows:
# 1. A word can be constructed from sequentially adjacent spots in the matrix,
# where adjacent means moving horizontally, vertically, or diagonally in any direction.
# 2. A word cannot use the same location twice to construct itself.
#
# The rules are similar to the game of Boggle. So for the example above, all the words exist in that matrix
# so your program should return the string true. If all the words cannot be found, then return
# a comma separated string of the words that cannot be found, in the order they appear in the dictionary.


class Trie:
    def __init__(self):
        self.character = {}
        self.is_leaf = False


def insert(root, string):
    curr = root
    for character in string:
        curr = curr.character.setdefault(character, Trie())
    curr.is_leaf = True


def is_allowed(x, y, processed, board, ch):
    return (0 <= x < len(processed)) and \
           0 <= y < len(processed[0]) and \
           not processed[x][y] and (board[x][y] == ch)


def search_words(root, brd, i, j, processed, path, result):
    row_moves = [-1, -1, -1, 0, 1, 0, 1, 1]
    col_moves = [-1, 1, 0, -1, -1, 1, 0, 1]

    if root.is_leaf:
        result.add(path)

    processed[i][j] = True

    for key, value in root.character.items():
        for k in range(len(row_moves)):
            if is_allowed(i + row_moves[k], j + col_moves[k], processed, brd, key):
                search_words(
                    value,
                    brd,
                    i + row_moves[k],
                    j + col_moves[k],
                    processed,
                    path + key,
                    result
                )

    processed[i][j] = False


def matrix_challenge(str_arr: list) -> str:
    board = [list(line) for line in str_arr[0].split(", ")]

    words = str_arr[-1].split(",")

    found_words = set()

    root = Trie()
    for word in words:
        insert(root, word)

    processed = [[False for x in range(4)] for y in range(4)]

    for i in range(4):
        for j in range(4):
            curr_char = board[i][j]

            if curr_char in root.character:
                search_words(root.character[curr_char], board, i, j, processed, curr_char, found_words)

    result = []

    for word in words:
        if word not in found_words:
            result.append(word)

    if result:
        return ",".join(result)

    return "true"
