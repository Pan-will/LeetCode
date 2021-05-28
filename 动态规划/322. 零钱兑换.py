"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1
"""
import math


# 备忘录解法，自顶向下
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 备忘录
        memo = [-666 for _ in range(amount + 1)]
        return self.helper(memo, coins, amount)

    def helper(self, memo, coins, amount):
        # base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if memo[amount] != -666:
            return memo[amount]
        res = 99999
        for coin in coins:
            subproblem = self.helper(memo, coins, amount - coin)
            if subproblem == -1:
                continue
            res = min(res, subproblem+1)
        if res == 99999:
            memo[amount] = -1
        else:
            memo[amount] = res
        return memo[amount]


if __name__ == '__main__':
    s = Solution()
    s.coinChange(coins=[1, 2, 5], amount=11)
