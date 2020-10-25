"""
你正在经营一座摩天轮，该摩天轮共有 4 个座舱 ，每个座舱 最多可以容纳 4 位游客 。你可以 逆时针 轮转座舱，但每次轮转都需要支付一定的运行成本 runningCost 。摩天轮每次轮转都恰好转动 1 / 4 周。

给你一个长度为 n 的数组 customers ， customers[i] 是在第 i 次轮转（下标从 0 开始）之前到达的新游客的数量。这也意味着你必须在新游客到来前轮转 i 次。每位游客在登上离地面最近的座舱前都会支付登舱成本 boardingCost ，一旦该座舱再次抵达地面，他们就会离开座舱结束游玩。

你可以随时停下摩天轮，即便是 在服务所有游客之前 。如果你决定停止运营摩天轮，为了保证所有游客安全着陆，将免费进行所有后续轮转 。注意，如果有超过 4 位游客在等摩天轮，那么只有 4 位游客可以登上摩天轮，其余的需要等待 下一次轮转 。

返回最大化利润所需执行的 最小轮转次数 。 如果不存在利润为正的方案，则返回 -1 。

示例：
输入：customers = [8,3], boardingCost = 5, runningCost = 6
输出：3
解释：座舱上标注的数字是该座舱的当前游客数。
1. 8 位游客抵达，4 位登舱，4 位等待下一舱，摩天轮轮转。当前利润为 4 * $5 - 1 * $6 = $14 。
2. 3 位游客抵达，4 位在等待的游客登舱，其他 3 位等待，摩天轮轮转。当前利润为 8 * $5 - 2 * $6 = $28 。
3. 最后 3 位游客登舱，摩天轮轮转。当前利润为 11 * $5 - 3 * $6 = $37 。
轮转 3 次得到最大利润，最大利润为 $37 。
"""


class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        if not customers:
            return 0
        # 返回值——转动次数
        res = 0
        # 当前为止的总利润
        profit = 0
        # 下一轮转动前在等待的游客数
        curCurs = 0
        for i, item in enumerate(customers):
            # 本次转动在等待上来的所有游客
            temp = item + curCurs
            if temp > 4:
                curCurs = temp - 4
                profit = profit + 4 * boardingCost - runningCost
            else:
                curCurs = 0
                profit = profit + temp * boardingCost - runningCost
            res += 1
        if curCurs and curCurs > 4:
            while curCurs > 4:
                res += 1
                profit = profit + 4 * boardingCost - runningCost
                curCurs -= 4
        # 暂存满仓位的利润
        tempProfit = profit
        if curCurs and curCurs <= 4:
            res += 1
            profit = profit + curCurs * boardingCost - runningCost
        # 不存在最大利润
        if profit < 0:
            return -1
        if tempProfit >= profit:
            return res - 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minOperationsMaxProfit(customers=[10, 10, 1, 0, 0], boardingCost=4, runningCost=4))
