# coding=utf-8


class Solution(object):

    """
    118. 杨辉三角
    (https://leetcode-cn.com/problems/pascals-triangle/description/)

    给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

    示例:

    输入: 5
    输出:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    """

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def next_row(nums):
            mid = [nums[i] + nums[i + 1] for i in range(0, len(nums) - 1)]
            return [1] + mid + [1]

        rows, row = [], [1]
        if numRows > 0:
            for n in range(0, numRows):
                rows.append(row)
                row = next_row(row)

        return rows
