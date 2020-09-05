"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

 示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        if cost[0] < cost[1]:
            ans += cost[0]
            i = 0
        else:
            ans += cost[1]
            i = 1
        while i < len(cost) - 2:
            if cost[i + 1] < cost[i + 2]:
                ans += cost[i + 1]
                i += 1
            else:
                ans += cost[i + 2]
                i += 2
        return ans

    def minCostClimbingStairs2(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost1 = cost2 = 0
        for i in cost:
            cost1, cost2 = i + min(cost1, cost2), cost1
        return min(cost1, cost2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs2([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
