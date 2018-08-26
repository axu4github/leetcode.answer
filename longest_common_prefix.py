# coding=utf-8


class Solution(object):

    """
    14. 最长公共前缀
    (https://leetcode-cn.com/problems/longest-common-prefix/description/)

    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。

    示例 1:

    输入: ["flower","flow","flight"]
    输出: "fl"
    示例 2:

    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
    说明:

    所有输入只包含小写字母 a-z 。
    """

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i, lcp = 0, ""
        while True:
            try:
                _strs = list(set(map(lambda _str: _str[i], strs)))
            except Exception:
                break

            if len(_strs) != 1:
                break
            else:
                lcp += _strs[0]
                i += 1

        return lcp
