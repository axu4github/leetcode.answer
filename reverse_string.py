# coding=utf-8


class Solution(object):

    """
    344. 反转字符串
    (https://leetcode-cn.com/problems/reverse-string/description/)

    编写一个函数，其作用是将输入的字符串反转过来。

    示例 1:

    输入: "hello"
    输出: "olleh"
    示例 2:

    输入: "A man, a plan, a canal: Panama"
    输出: "amanaP :lanac a ,nalp a ,nam A"
    """

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
