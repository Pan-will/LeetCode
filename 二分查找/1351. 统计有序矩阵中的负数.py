"""
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
请你统计并返回 grid 中 负数 的数目。

示例 1：
输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。
"""


class Solution(object):
    # 二分法
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for nums in grid:
            if nums[0] < 0:
                ans += len(nums)
                continue
            if nums[-1] >= 0:
                continue
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = int(i + (j - i) / 2)
                if nums[mid] >= 0:
                    i = mid + 1
                else:
                    j = mid - 1
            if nums[i] < 0:
                ans += len(nums) - i
        return ans

    # 暴力
    def countNegatives2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            if grid[i][0] < 0:
                ans += len(grid[i])
            else:
                for j in range(len(grid[i])):
                    if grid[i][j] < 0:
                        ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.countNegatives(
        [[4, 3, 3, 1, 1], [1, 0, 0, -1, -1], [-2, -2, -2, -2, -3], [-2, -2, -2, -3, -3], [-3, -3, -3, -3, -3]]))
