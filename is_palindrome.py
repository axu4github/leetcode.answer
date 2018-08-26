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
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            _str = str(x)
            _str_len = len(_str)
            mid = _str_len / 2
            if _str_len % 2 == 0:
                return _str[0:mid] == _str[mid:][::-1]
            else:
                return _str[0:mid + 1] == _str[mid:][::-1]
