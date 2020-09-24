"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

 

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
"""

"""动态规划"""
# 思路：设f[i][j]是寻找到第i层时的最短路径和，c[i][j]是当前的第i层第j个元素，i和j都从0开始计数。
#   一般情况下，f[i][j]的取值和肩上的两个元素有关，则f[i][j] = c[i][j] + min{f[i-1][j-1], f[i-1][j]}
#   特殊情况：j处于当前层的两个端点处时，那么只有可能从上一层的端点处传下来；
#           当j = 0时：上一层只有可能从c[i-1][0]传下来，则f[i][j] = c[i][0] + f[i-1][0]；
#           当j = i时：上一层只有可能从c[i-1][j-1]传下来，则f[i][j] = c[i][j] + f[i-1][j-1] = c[i][i] + f[i-1][j-1]；
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        n = len(triangle)
        # 构造n*n规模的记录矩阵
        f = [[0]*n for i in range(n)]
        # 第一层只有一个元素，便只有一个选择
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            # 特判：j=0的情况
            f[i][0] = f[i-1][0] + triangle[i][0]
            # 一般情况：取肩上两个元素的较小者，再加上当前元素
            for j in range(1, i):
                f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]
            # 特判：j=i的情况
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        return [min(f[n-1])]



if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
