"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
"""


class Solution(object):
    """
    这里对i和k都加入了等于0的状态
    而且k的遍历要是从大到小的, k代表剩余交易次数, 完整的买和卖算一次, 因此只在买的时候k-1
    """

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        l = len(prices)
        dp = [[[0, 0], [0, 0], [0, 0]] for _ in range(l + 1)]
        # float('-inf')表负无穷
        for k in range(3):
            dp[0][k][1] = float('-inf')
        for i in range(l + 1):
            dp[i][0][1] = float('-inf')
        for i in range(1, l + 1):
            # 从后往前遍历
            for k in range(2, 0, -1):
                # sell
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i - 1])
                # buy
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i - 1])
        # 不是返回dp[-1][0][0]!!! 意思是返回最后一天有两次交易次数且手里没股票的最大利润
        return dp[-1][2][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
