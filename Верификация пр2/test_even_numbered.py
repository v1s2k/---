import unittest
from even_numbered import Even


class TestSet(unittest.TestCase):
    def setUp(self):
        self.very = Even()

    def test1(self):
        self.assertEqual(self.very.very_even(44), "четное")

    def test2(self):
        self.assertEqual(self.very.very_even(21), "нечетное")


if __name__ == "__main__":
    unittest.main()
