# coding=utf-8


class Solution(object):

    """
    1. 两数之和 (https://leetcode-cn.com/problems/two-sum/description/)

    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

    你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

    示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, one_num in enumerate(nums):
            for j, two_num in enumerate(nums[i + 1:]):
                if sum((one_num, two_num)) == target:
                    return [i, i + j + 1]

        return [None, None]

    def twoSumPerformance(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, one_num in enumerate(nums):
            two_num = target - one_num
            if two_num in nums[i + 1:]:
                return [i, nums.index(two_num, i + 1)]

        return [None, None]
