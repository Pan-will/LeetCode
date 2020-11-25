"""
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
请你计算 最多 能喝到多少瓶酒。
 

示例 1：
输入：numBottles = 9, numExchange = 3
输出：13
解释：你可以用 3 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 9 + 3 + 1 = 13 瓶酒。
"""


class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # 特判
        if numExchange > numBottles:
            return numBottles
        # 记录每轮喝了多少瓶酒
        boots = [numBottles]
        # 记录当前的空酒瓶
        empty = numBottles
        while empty >= numExchange:
            # 本轮兑换的新酒
            boot = empty // numExchange
            # 新酒瓶数加到boots中
            boots.append(boot)
            # 本轮兑换后的空酒瓶 = 兑换时剩余的空酒瓶 + 兑换所得的酒瓶数
            empty = empty % numExchange + boot
        # print(boots)
        return sum(boots)


if __name__ == '__main__':
    s = Solution()
    print(s.numWaterBottles(2, 3))
