# coding=utf-8

from two_sum import Solution as twoSumSolution
from longest_common_prefix import Solution as LongestCommonPrefix
from reverse import Solution as Reverse
from is_palindrome import Solution as IsPalindrome
from is_valid import Solution as IsValid
import unittest

IGNORE_OTHER_PERFORMANCE_TESTS = True


class TestPython(unittest.TestCase):

    def test_list(self):
        self.assertEqual(range(1, 10), range(0, 10)[1:])

    def test_list_index(self):
        self.assertEqual(4, ([0, 0, 1, 1, 2, 2].index(2)))
        self.assertEqual(3, ([0, 0, 1, 1, 2, 2].index(1, 3)))

    def test_list_in(self):
        self.assertTrue(2 in [0, 0, 1, 1, 2, 2])

    def test_map(self):
        strs, i = ["flower", "flow", "flight"], 0

        self.assertEqual(["f", "f", "f"], map(lambda x: x[i], strs))
        self.assertEqual(strs, strs)

        try:
            map(lambda x: x[4], strs)
        except Exception as e:
            self.assertTrue("out of" in str(e))

    def test_str(self):
        self.assertEqual("321-", "-123"[::-1])
        self.assertEqual("321", "-123"[1:][::-1])

    def test_int(self):
        self.assertEqual(2147483648, 2**31)
        self.assertEqual(0, 1122 % 11)

    def test_range(self):
        self.assertTrue(22 in range(11, 100, 11))
        self.assertEqual(9, len(range(11, 100, 11)))


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

    def test_two_sum_performance_correct(self):
        self.assertEqual(
            [0, 1], self.ts.twoSumPerformance([2, 7, 9, 11, 15], 9))
        self.assertEqual(
            [1, 2], self.ts.twoSumPerformance([2, 0, 9, 11, 15], 9))
        self.assertEqual(
            [1, 4], self.ts.twoSumPerformance([2, 0, 0, 11, 9], 9))
        self.assertEqual([1, 2], self.ts.twoSumPerformance([3, 2, 4], 6))
        self.assertEqual([None, None], self.ts.twoSumPerformance([], 9))
        self.assertEqual([None, None], self.ts.twoSumPerformance([9], 9))
        self.assertEqual([0, 3], self.ts.twoSumPerformance([0, 4, 3, 0], 0))
        self.assertEqual(
            [2, 4], self.ts.twoSumPerformance([-1, -2, -3, -4, -5], -8))

    def test_two_sum_performance(self):
        if not IGNORE_OTHER_PERFORMANCE_TESTS:
            nums = filter(lambda num: num % 2 == 0, range(0, 25197))
            nums[8012], target = -1, 16021
            self.assertEqual(
                [8011, 8012], self.ts.twoSumPerformance(nums, target))


class TestLongestCommonPrefix(unittest.TestCase):

    def setUp(self):
        self.lcp = LongestCommonPrefix()

    def test_longest_common_prefix(self):
        self.assertEqual(
            "fl", self.lcp.longestCommonPrefix(["flower", "flow", "flight"]))
        self.assertEqual(
            "", self.lcp.longestCommonPrefix(["dog", "racecar", "car"]))


class TestReverse(unittest.TestCase):

    def setUp(self):
        self.r = Reverse()

    def test_reverse(self):
        self.assertEqual(321, self.r.reverse(123))
        self.assertEqual(-321, self.r.reverse(-123))
        self.assertEqual(21, self.r.reverse(120))


class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        self.ip = IsPalindrome()

    def test_is_palindrome(self):
        self.assertTrue(self.ip.isPalindrome(121))
        self.assertTrue(not self.ip.isPalindrome(-121))
        self.assertTrue(not self.ip.isPalindrome(10))
        self.assertTrue(self.ip.isPalindrome(313))

    def test_is_palindrome_for_int(self):
        self.assertTrue(self.ip.isPalindromeForInt(121))
        self.assertTrue(not self.ip.isPalindromeForInt(-121))
        self.assertTrue(not self.ip.isPalindromeForInt(10))
        self.assertTrue(self.ip.isPalindromeForInt(313))
        self.assertTrue(not self.ip.isPalindromeForInt(1122))
        self.assertTrue(self.ip.isPalindromeForInt(11))

    def test_fill_digits(self):
        self.assertEqual(11, self.ip.fill_digits(1, 1))
        self.assertEqual(111, self.ip.fill_digits(11, 2))
        self.assertEqual(
            1111, self.ip.fill_digits(self.ip.fill_digits(11, 2), 3))
        self.assertEqual(11122, self.ip.fill_digits(1122, 4))


class TestIsValid(unittest.TestCase):

    def setUp(self):
        self.iv = IsValid()

    def test_is_valid(self):
        self.assertTrue(self.iv.isValid("()"))
        self.assertTrue(self.iv.isValid("()[]{}"))
        self.assertTrue(not self.iv.isValid("(]"))
        self.assertTrue(not self.iv.isValid("([)]"))
        self.assertTrue(self.iv.isValid("{[]}"))
        self.assertTrue(not self.iv.isValid("]"))
        self.assertTrue(self.iv.isValid(""))
        self.assertTrue(not self.iv.isValid("[])"))


if __name__ == "__main__":
    unittest.main()
