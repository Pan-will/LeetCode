#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算01背包问题的结果
# @param V int整型 背包的体积
# @param n int整型 物品的个数
# @param vw int整型二维数组 第一维度为n,
# 第二维度为2的二维数组,vw[i][0],
# vw[i][1]分别描述i+1个物品的vi,wi
# @return int整型
#
class Solution:
    def knapsack(self, V, n, vw):
        if n==0 or V==0 or len(vw)==0: return 0
        dp = [[0 for _ in range(V+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, V+1):
                if j - vw[i-1][0] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j - vw[i-1][0]] + vw[i-1][1], dp[i-1][j])
        return dp[n][V]


if __name__ == '__main__':
    s = Solution()
    print(s.knapsack(10, 2, [[1, 3], [10, 4]]))
