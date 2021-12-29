import unittest
from Matrix_challenge_boggle_type import matrix_challenge


class MatrixChallengeTest(unittest.TestCase):

    def test_matrix_challenge(self):
        with self.subTest():
            self.assertEqual(
                matrix_challenge(["rbfg, ukop, fgub, mnry", "bog,bop,gup,fur,ruk"]),
                "true",
                "Should be equal to 'true'"
            )

        with self.subTest():
            self.assertEqual(
                matrix_challenge(["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,tall,true,trum"]),
                "true",
                "Should be equal to 'true'"
            )

        with self.subTest():
            self.assertEqual(
                matrix_challenge(["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,rumk,tall,true,trum,yes"]),
                "rumk,yes",
                "Should be equal to 'rumk,yes'"
            )


if __name__ == '__main__':
    unittest.main()
