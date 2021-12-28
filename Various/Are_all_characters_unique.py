# Write a function that checks whether all characters in a given string are unique

import unittest


def are_all_characters_unique(src_str):

    if type(src_str) != str:
        raise TypeError("Argument must be of string type")

    return len(src_str) == len(set(src_str))


class AreAllCharsUniqueTest(unittest.TestCase):

    def test_type(self):
        self.assertRaises(
            TypeError,
            are_all_characters_unique,
            1
        )

    def test_chars_uniqueness(self):
        with self.subTest():
            self.assertTrue(
                are_all_characters_unique("abcdefghijklmn123"),
            )

        with self.subTest():
            self.assertFalse(
                are_all_characters_unique("abcdefghijklmn123ab"),
            )
