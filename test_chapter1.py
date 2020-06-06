import unittest
import time
from solution_chapter1 import total_emeralds


class TestChapter1(unittest.TestCase):

    def test_total_emeralds0(self):
        self.assertEqual(total_emeralds, 30, "Should be 60 emeralds")


if __name__ == '__main__':
    time.sleep(0.1)
    unittest.main()
