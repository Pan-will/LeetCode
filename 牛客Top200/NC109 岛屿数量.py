"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

"""


class Solution(object):
    def numIslands(self, grid):
        row = len(grid)
        if not row: return 0
        col = len(grid[0])
        # 初始化一个二维数组，初始用0填充
        isUsed = [[0 for _ in range(col)] for _ in range(row)]
        res = 0
        for i in range(row):
            for j in range(col):
                if not isUsed[i][j]:
                    if grid[i][j] == 1:
                        self.dfs(grid, i, j, isUsed)
                        res += 1
        return res

    def dfs(self, grid, i, j, isUsed):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or isUsed[i][j]:
            return
        isUsed[i][j] = 1

        self.dfs(grid, i + 1, j, isUsed)
        self.dfs(grid, i, j + 1, isUsed)
        self.dfs(grid, i - 1, j, isUsed)
        self.dfs(grid, i, j - 1, isUsed)


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([[1, 1, 0, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 1, 1]]))
    print(s.numIslands([[1]]))