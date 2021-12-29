# Write a function that checks whether it is possible
# to make a palindrome from a given string


def is_palindrome(src_str: str) -> bool:
    if type(src_str) != str:
        raise TypeError("Argument must be of string type")

    str_as_dict = {}

    for symb in src_str:
        str_as_dict[symb] = str_as_dict.get(symb, 0) + 1

    count = 0
    for value in str_as_dict.values():
        if value % 2 != 0:
            count += 1

    return count <= 1



