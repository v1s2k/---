import unittest
from origin_word import words


class TestSet(unittest.TestCase):
    def setUp(self):
        self.check = words()

    def test1(self):

        self.assertEqual(self.check.origin_word("busa"), True)

    def test2(self):

        self.assertEqual(self.check.origin_word("www"), False)


if __name__ == "__main__":
    unittest.main()
