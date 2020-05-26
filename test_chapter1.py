import unittest
import time
from chapter1 import chickens_to_emeralds, total_emeralds


class TestChapter1(unittest.TestCase):

    def test_chickens_to_emeralds(self):
        self.assertEqual(chickens_to_emeralds(70), 5.0, "Should be 5.0 emeralds")

    def test_total_emeralds1(self):
        self.assertEqual(total_emeralds(30, 30, 30), 5.0, "Should be 5.0 emeralds")

    def test_total_emeralds2(self):
        self.assertEqual(total_emeralds(30, 30, 30), 5.0, "Should be 5.0 emeralds")

    def test_total_emeralds3(self):
        self.assertEqual(total_emeralds(30, 30, 30), 5.0, "Should be 5.0 emeralds")

    def test_total_emeralds4(self):
        self.assertEqual(total_emeralds(30, 30, 30), 5.0, "Should be 5.0 emeralds")

    def test_total_emeralds5(self):
        self.assertEqual(total_emeralds(30, 30, 30), 5.0, "Should be 5.0 emeralds")

if __name__ == '__main__':
    time.sleep(0.1)
    unittest.main()
