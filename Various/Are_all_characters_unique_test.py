import unittest
from Are_all_characters_unique import are_all_characters_unique


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


if __name__ == '__main__':
    unittest.main()
