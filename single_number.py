# coding=utf-8

import collections


class Solution(object):

    """
    136. 只出现一次的数字
    (https://leetcode-cn.com/problems/single-number/description/)

    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

    说明：
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

    示例 1:
    输入: [2,2,1]
    输出: 1

    示例 2:
    输入: [4,1,2,1,2]
    输出: 4
    """

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _dict = {}
        for num in nums:
            if num in _dict:
                _dict[num] += 1
                if _dict[num] > 1:
                    del _dict[num]
            else:
                _dict[num] = 1

        return _dict.keys()[0]

    def normalSingleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums)) * 2 - sum(nums)
