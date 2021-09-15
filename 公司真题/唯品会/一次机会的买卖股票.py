"""
思路：
1、将prices升序排列；
2、用price遍历排序后的prices，取price在原list中的下标i;
3、在原list中截取下标i之后的元素，取其中最大值max(temp[i:])；
4、计算当前利润：max(temp[i:]) - price，存入ans[]中；
5、返回ans中的最大值。
"""


class Solution(object):
    def maxProfit(self, prices):
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
    # print(solution.maxProfit2([7, 1, 5, 3, 6, 4]))
    # print(solution.maxProfit([4, 3, 2, 1]))
    print(solution.maxProfit([1, 4, 2]))
