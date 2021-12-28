# Write a function that checks whether it is possible
# to make a palindrome from a given string

import unittest


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


class IsPalindromeTest(unittest.TestCase):

    def test_arg_type(self):
        self.assertRaises(
            TypeError,
            is_palindrome,
            1
        )

    def test_is_palindrome(self):
        with self.subTest():
            self.assertTrue(
                is_palindrome("asasu")
            )
        with self.subTest():
            self.assertFalse(
                is_palindrome("asasua")
            )
