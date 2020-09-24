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


class Solution(object):
    # 从下往上考虑
    # 思路：第一层不用考虑，第二层在当前位置（triangle[i][j]）选两只脚中较小的一个加到当前位置；
    # 依次类推，知道第二层就能推知第三层的值，直到最高层。
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        # 设置n*n规模的记录矩阵
        dp = [[0] * n for _ in range(n)]
        # 从下往上考虑，所以倒序for循环，range()的前两个参数是遍历区间，前开后闭；第三个参数是步长。
        for i in range(n - 1, -1, -1):
            # 每一层同样也是倒序for循环
            for j in range(len(triangle[i]) - 1, -1, -1):
                # 第一层不用考虑，直接赋值
                if i == n - 1:
                    dp[i][j] = triangle[i][j]
                # 往上每一层，当前元素与两只脚的较小者相加，并赋值给记录矩阵
                else:
                    dp[i][j] = min(dp[i + 1][j + 1], dp[i + 1][j]) + triangle[i][j]
        # 遍历到最高层，那此时的唯一一个元素就是最短路径和
        return dp[0][0]

    # 从上往下考虑
    # 思路：设f[i][j]是寻找到第i层时的最短路径和，c[i][j]是当前的第i层第j个元素，i和j都从0开始计数。
    #   一般情况下，f[i][j]的取值和肩上的两个元素有关，则f[i][j] = c[i][j] + min{f[i-1][j-1], f[i-1][j]}
    #   特殊情况：j处于当前层的两个端点处时，那么只有可能从上一层的端点处传下来；
    #           当j = 0时：上一层只有可能从c[i-1][0]传下来，则f[i][j] = c[i][0] + f[i-1][0]；
    #           当j = i时：上一层只有可能从c[i-1][j-1]传下来，则f[i][j] = c[i][j] + f[i-1][j-1] = c[i][i] + f[i-1][j-1]；
    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        n = len(triangle)
        # 设置n*n规模的记录矩阵
        f = [[0] * n for i in range(n)]
        # 第一层只有一个元素，便只有一个选择
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            # 特判：j=0的情况
            f[i][0] = f[i - 1][0] + triangle[i][0]
            # 一般情况：取肩上两个元素的较小者，再加上当前元素
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            # 特判：j=i的情况
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        return [min(f[n - 1])]


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
