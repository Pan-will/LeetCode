"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：不能同时参与多笔交易（必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释:
在第 2 天（价格 = 1）的时候买入，在第 3 天（价格 = 5）的时候卖出, 这笔获得利润 = 5-1 = 4 。
在第 4 天（价格 = 3）的时候买入，在第 5 天（价格 = 6）的时候卖出, 这笔获得利润 = 6-3 = 3 。
两次总利润 = 4+3 = 7

思路：
想到：prices中一列数字，任取一个为买入价格buy，在其右边任取一个为卖出价格sell；
取[buy,...,sell]区间中相邻数字之差，这些差值求和为sum，则必有sell-buy = sum；

本题中求最大收益，所以遍历prices，找到prices[i]-prices[i-1] > 0的位置作为买入点。
此后一直遍历到prices末尾，将相邻两个元素的差加到ans中，最后得ans即为最大利润。

两种方法都通过。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        ans = 0
        while i < len(prices) - 1:
            if prices[i + 1] < prices[i]:
                i += 1
                continue
            else:
                buy = prices[i]
                ans += prices[i + 1] - buy
                i += 1
        return ans

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit2([7, 1, 5, 3, 4, 6]))
    # print(solution.maxProfit2([3, 3, 5, 0, 0, 3, 1, 4]))
