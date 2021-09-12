# @param grid int整型二维数组 二维数组
# @param x int整型
# @param y int整型
# @return int整型
class Solution:
    def solution(self, grid, x, y):
        if not grid:
            return 0
        if x == 0 and y == 0:
            return grid[x][y]
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        for c in range(1, col):
            dp[0][c] = dp[0][c - 1] + grid[0][c]
        for r in range(1, row):
            dp[r][0] += dp[r - 1][0] + grid[r][0]
        for r in range(1, row):
            for c in range(1, col):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
        return dp[x][y]


if __name__ == '__main__':
    s = Solution()
    print(s.solution([[1, 2, 3, 6, 2, 8, 1], [4, 8, 2, 4, 3, 1, 9], [1, 5, 3, 7, 9, 3, 1], [4, 9, 2, 1, 6, 9, 5],
                      [7, 6, 8, 4, 7, 2, 6], [2, 1, 6, 2, 4, 8, 7], [8, 4, 3, 9, 2, 5, 8]], 0, 0))
    print(s.solution([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2))
