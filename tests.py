# coding=utf-8

from two_sum import Solution as twoSumSolution
import unittest


class TestPython(unittest.TestCase):

    def test_list(self):
        self.assertEqual(range(1, 10), range(0, 10)[1:])


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.ts = twoSumSolution()

    def test_two_sum(self):
        self.assertEqual([0, 1], self.ts.twoSum([2, 7, 9, 11, 15], 9))
        self.assertEqual([1, 2], self.ts.twoSum([2, 0, 9, 11, 15], 9))
        self.assertEqual([1, 4], self.ts.twoSum([2, 0, 0, 11, 9], 9))
        self.assertEqual([1, 2], self.ts.twoSum([3, 2, 4], 6))
        self.assertEqual([None, None], self.ts.twoSum([], 9))
        self.assertEqual([None, None], self.ts.twoSum([9], 9))


if __name__ == "__main__":
    unittest.main()
