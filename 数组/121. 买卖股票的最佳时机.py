"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
返回所获最大利润值。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

思路：
1、将prices升序排列；
2、用price遍历排序后的prices，取price在原list中的下标i;
3、在原list中截取下标i之后的元素，取其中最大值max(temp[i:])；
4、计算当前利润：max(temp[i:]) - price，存入ans[]中；
5、返回ans中的最大值。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 存放利润，返回其中最大值
        ans = []
        # 用temp暂存原list
        temp = prices
        # 升序排列
        prices = sorted(prices, reverse=False)
        # 没有交易完成，利润为0
        if prices[::-1] == temp:
            return 0
        # 遍历升序排列的prices
        for price in prices:
            # 取当前price在原list中的下标
            i = temp.index(price)
            # 如果最低价是原list的最后一个元素，跳过
            if i == len(temp) - 1:
                continue
            # 取i往后的最大价格与当前价格作差，即利润，存入ans中
            ans.append(max(temp[i:]) - price)
        return max(ans)

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 返回值
        ans = 0
        # 初始首元素设为买入值
        buy = prices[0]
        # 从第一个元素开始遍历prices
        for i in range(1, len(prices)):
            # 买入值取当前元素和之前记录的买入值之间的最小值
            buy = min(buy, prices[i])
            # 利润取卖出价格减买入价格中的最大值
            ans = max(prices[i] - buy, ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit2([7, 1, 5, 3, 6, 4]))
    # print(solution.maxProfit([4, 3, 2, 1]))
