import unittest
import time
from chapter1 import chickens_to_emeralds, total_emeralds


class TestChapter1(unittest.TestCase):

    def test_chickens_to_emeralds(self):
        self.assertEqual(chickens_to_emeralds(70), 5, "Should be 5 emeralds")

    def test_total_emeralds0(self):
        self.assertEqual(total_emeralds(35, 20, 8), 8, "Should be 8 emeralds")

    def test_total_emeralds1(self):
        self.assertEqual(total_emeralds(70, 70, 70), 32, "Should be 32 emeralds")

    def test_total_emeralds2(self):
        self.assertEqual(total_emeralds(14, 4, 7), 3, "Should be 3 emeralds")

    def test_total_emeralds3(self):
        self.assertEqual(total_emeralds(28, 12, 21), 8, "Should be 8 emeralds")

    def test_total_emeralds4(self):
        self.assertEqual(total_emeralds(14, 0, 10), 2, "Should be 1 emerald")

    def test_total_emeralds5(self):
        self.assertEqual(total_emeralds(30, 30, 35), 14, "Should be 14 emeralds")


if __name__ == '__main__':
    time.sleep(0.1)
    unittest.main()
