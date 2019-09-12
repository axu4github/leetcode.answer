# coding=utf-8


class Solution(object):

    """
    695. 岛屿的最大面积
    (https://leetcode-cn.com/problems/max-area-of-island/description/)

    给定一个包含了一些 0 和 1的非空二维数组 grid ,
    一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。
    你可以假设二维矩阵的四个边缘都被水包围着。

    找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

    示例 1:

    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

    示例 2:

    [[0,0,0,0,0,0,0,0]]
    对于上面这个给定的矩阵, 返回 0。

    注意: 给定的矩阵grid 的长度和宽度都不超过 50。
    """

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # TODO
        def is_area(num):
            return num == 1

        def get_link(area):
            (x, y), links = area, []
            offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for offset_x, offset_y in offsets:
                area_offset = (x + offset_x, y + offset_y)
                if area_offset in areas:
                    links.append(area_offset)
                    del areas[area_offset]

            return links

        areas = {}
        for x, nums in enumerate(grid):
            for y, num in enumerate(nums):
                if is_area(num):
                    areas[(x, y)] = num

        # print(areas.keys())

        return 6
