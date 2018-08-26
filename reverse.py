# coding=utf-8


class Solution(object):

    """
    7. 反转整数
    (https://leetcode-cn.com/problems/reverse-integer/description/)

    给定一个 32 位有符号整数，将整数中的数字进行反转。

    示例 1:

    输入: 123
    输出: 321

    示例 2:

    输入: -123
    输出: -321

    示例 3:

    输入: 120
    输出: 21
    注意:

    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
    """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        _str, is_less_zero = str(x), False
        if _str[0] == "-":
            is_less_zero = True
            _str = _str[1:][::-1]
        else:
            _str = _str[::-1]

        if _str[0] == "0":
            _str = _str[1:]

        if is_less_zero:
            _str = "-{0}".format(_str)

        try:
            res = int(_str)
            if res >= 2 ** 31 or res <= -1 * 2 ** 31:
                res = 0
        except Exception:
            return 0

        return res
