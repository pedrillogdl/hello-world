import unittest
import math


class TestMathCeil(unittest.TestCase):
    def test_happyPath(self):
        # Right: Testing that the app is doing what it should do
        # testing a number near the floor, near the ceil, in the middle,
        # an int number and  then a negative number,
        # also testing that is not going to the floor
        self.assertEqual(math.ceil(1.2), 2)
        self.assertEqual(math.ceil(3.9), 4)
        self.assertEqual(math.ceil(5.5), 6)
        self.assertEqual(math.ceil(11), 11)
        self.assertEqual(math.ceil(-1.2), -1)
        self.assertNotEqual(math.ceil(-1.2), -2)
        self.assertNotEqual(math.ceil(3.1), 3)

    def test_boundary(self):
        # B: Testing the boundaries, an invalid value,
        # a big negative number and a big integer
        with self.assertRaises(Exception):
            math.ceil(a)
        self.assertEqual(math.ceil(213432431243124.12), 213432431243125)
        self.assertEqual(math.ceil(-12354325432452.2334534534), -12354325432452)

    def test_inverse(self):
        # I:Comparing the math ceil with its counterpart that is math floor
        self.assertNotEqual(math.ceil(12.5), math.floor(12.5))
        self.assertNotEqual(math.ceil(34.93554374567), math.floor(34.93554374567))
        self.assertNotEqual(math.ceil(100.1123123), math.floor(100.1123123))


if __name__ == '__main__':
    unittest.main()
