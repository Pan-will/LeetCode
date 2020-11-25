"""
数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。

你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：

将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
最开始的时候，同一位置上也可能放着两个或者更多的筹码。
返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。

示例 1：
输入：chips = [1,2,3]
输出：1
解释：第二个筹码移动到位置三的代价是 1，第一个筹码移动到位置三的代价是 0，总代价为 1。

示例 2：
输入：chips = [2,2,2,3,3]
输出：2
解释：第四和第五个筹码移动到位置二的代价都是 1，所以最小总代价为 2。
"""

"""
思路：贪心法：由局部最优扩展到全局最优。
1、走两步代价为0，由此我们可以把所有奇数位置的元素都移动到1号位置，所有偶数位置的元素都移动到2号位置，代价为0；
2、两个位置合并，要代价最小：那个位置元素少就移动那个位置呗。
所以第二步就是比较两个位置谁的元素少，取较小者即是返回值。
"""


class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        ji = 0
        ou = 0
        for poi in position:
            if poi & 1:
                ji += 1
            else:
                ou += 1
        return min(ji, ou)


if __name__ == '__main__':
    s = Solution()
    print(s.minCostToMoveChips([2, 2, 2, 3, 3]))
    print(s.minCostToMoveChips([1, 2, 3]))
    print(s.minCostToMoveChips([1,2,2,2,2]))
