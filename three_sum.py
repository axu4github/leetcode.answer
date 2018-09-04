# coding=utf-8


class Solution(object):

    """
    15. 三数之和
    (https://leetcode-cn.com/problems/3sum/description/)

    给定一个包含 n 个整数的数组 nums，
    判断 nums 中是否存在三个元素 a，b，c ，
    使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    """

    def two_sum(self, nums, target):
        all_res, _dict = [], {}
        for i, one_num in enumerate(nums):
            two_num = target - one_num
            if two_num in _dict:
                all_res.append([one_num, two_num])
            else:
                _dict[one_num] = i

        return all_res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        _dict, processed, nums = {}, {}, sorted(nums)
        for i, num in enumerate(nums):
            if num > 0 or num in processed:
                continue

            correct_nums = self.two_sum(nums[i + 1:], num * -1)
            if len(correct_nums) > 0:
                processed[num] = None
                for correct_num in correct_nums:
                    correct = tuple(sorted(correct_num + [num]))
                    if correct not in _dict:
                        _dict[correct] = None

        return map(lambda correct: list(correct), _dict.keys())
