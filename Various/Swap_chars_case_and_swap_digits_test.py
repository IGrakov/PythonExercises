import unittest
from Swap_chars_case_and_swap_digits import string_challenge


class StringChallengeTestCase(unittest.TestCase):

    def test_input_type(self):
        self.assertRaises(
            TypeError,
            string_challenge,
            1
        )

    def test_logic(self):
        with self.subTest():
            self.assertEqual(
                string_challenge("6Hello4 -8World, 7 yes3"),
                "4hELLO6 -8wORLD, 7 YES3",
                "Should be equal to '4hELLO6 -8wORLD, 7 YES3'"
            )

        with self.subTest():
            self.assertEqual(
                string_challenge("Hello -5LOL6"),
                "hELLO -6lol5",
                "Should be equal to 'hELLO -6lol5'"
            )

        with self.subTest():
            self.assertEqual(
                string_challenge("2S 6 du5d4e"),
                "2s 6 DU4D5E",
                "Should be equal to '2s 6 DU4D5E'"
            )

        with self.subTest():
            self.assertEqual(
                string_challenge("Hello -5L83V7L6"),
                "hELLO -6l73v8l5",
                "Should be equal to 'hELLO -6l73v8l5'"
            )

    def test_return_type(self):
        self.assertIsInstance(
            string_challenge("aaa"),
            str,
            "Should return str type"
        )


if __name__ == '__main__':
    unittest.main()
