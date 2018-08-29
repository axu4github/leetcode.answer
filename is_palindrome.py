# coding=utf-8


class Solution(object):

    """
    9. 回文数
    (https://leetcode-cn.com/problems/palindrome-number/description/)

    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:

    输入: 121
    输出: true

    示例 2:

    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

    示例 3:

    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。
    """

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    def number_of_digits(self, num, digits):
        for i in range(0, digits):
            new_num = num / 10
            res = num - new_num * 10
            num = new_num

        return res

    def get_digits_number(self, num):
        digits_number = 0
        while num != 0:
            num = num / 10
            digits_number += 1

        return digits_number

    def fill_digits(self, num, digits_number):
        digits = digits_number / 2 + 1
        return num * 10 + (num % 10**digits - num * 10 % 10**digits)

    def isPalindromeForInt(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            digits_number = self.get_digits_number(x)
            if digits_number % 2 == 0:
                mid_num = digits_number / 2
                (one_num, two_num) = (self.number_of_digits(x, mid_num),
                                      self.number_of_digits(x, mid_num + 1))
                return one_num == two_num and x % 11 == 0
            else:
                return self.fill_digits(x, digits_number) % 11 == 0
