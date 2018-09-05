# coding=utf-8


class Solution(object):

    """
    561. 数组拆分 I
    (https://leetcode-cn.com/problems/array-partition-i/description/)

    给定长度为 2n 的数组, 你的任务是将这些数分成 n 对
    例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

    示例 1:

    输入: [1,4,3,2]
    输出: 4

    解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
    """

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _sum, nums = 0, sorted(nums)
        for i in range(0, len(nums), 2):
            _sum += min(nums[i], nums[i + 1])

        return _sum
