import unittest
from Is_a_palindrome import is_palindrome


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


if __name__ == '__main__':
    unittest.main()
