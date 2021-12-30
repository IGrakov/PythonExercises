import unittest
from Find_amicable_pairs import (
    find_divisors,
    find_amicable_pairs
)


class FindAmicablePairsTest(unittest.TestCase):

    def test_find_divisors(self):
        with self.subTest():
            self.assertEqual(
                find_divisors(6),
                [1, 2, 3],
                "Should be equal to [1, 2, 3]"
            )

        with self.subTest():
            self.assertEqual(
                find_divisors(13),
                [1],
                "Should be equal to [1]"
            )

    def test_find_divisors_output_type(self):
        self.assertIsInstance(
            find_divisors(6),
            list,
            "Output should be of list type"
        )

    def test_find_amicable_pairs(self):
        with self.subTest():
            self.assertRaises(
                TypeError,
                find_amicable_pairs,
                "not an int"
            )

        with self.subTest():
            self.assertEqual(
                find_amicable_pairs(10),
                (0, [])
            )

        with self.subTest():
            self.assertEqual(
                find_amicable_pairs(230),
                (1, [(220, 284)])
            )

        with self.subTest():
            self.assertEqual(
                find_amicable_pairs(6_000),
                (4, [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564)])
            )

        with self.subTest():
            self.assertEqual(
                find_amicable_pairs(10_000),
                (5, [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368)])
            )

        with self.subTest():
            self.assertEqual(
                find_amicable_pairs(20_000),
                (8, [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368),
                     (10744, 10856), (12285, 14595), (17296, 18416)])
            )

    def test_find_amicable_number_output_type(self):
        output = find_amicable_pairs(230)

        with self.subTest():
            self.assertIsInstance(
                output,
                tuple,
                "Output should be of tuple type"
            )

        with self.subTest():
            self.assertIsInstance(
                output[0],
                int,
                "First element of output should be of int type"
            )

        with self.subTest():
            self.assertIsInstance(
                output[1],
                list,
                "Second element of output should be of list type"
            )

        with self.subTest():
            self.assertIsInstance(
                output[1][0],
                tuple,
                "Elements in list should be of tuple type"
            )


if __name__ == '__main__':
    unittest.main()
