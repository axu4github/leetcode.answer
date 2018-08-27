# coding=utf-8


class Solution(object):

    """
    20. 有效的括号
    (https://leetcode-cn.com/problems/valid-parentheses/description/)

    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

    示例 1:

    输入: "()"
    输出: true

    示例 2:

    输入: "()[]{}"
    输出: true

    示例 3:

    输入: "(]"
    输出: false

    示例 4:

    输入: "([)]"
    输出: false

    示例 5:

    输入: "{[]}"
    输出: true
    """

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ["(", "[", "{"]
        corrects = {"(": ")", "[": "]", "{": "}"}
        valids = []
        if len(s) == 0:
            return True

        for _str in s:
            if _str in left:
                valids.append(_str)
            elif len(valids) == 0 or _str != corrects[valids.pop()]:
                return False

        return len(valids) == 0
