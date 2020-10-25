"""
n 座城市和一些连接这些城市的道路 roads 共同组成一个基础设施网络。
每个 roads[i] = [ai, bi] 都表示在城市 ai 和 bi 之间有一条双向道路。

两座不同城市构成的 城市对 的 网络秩 定义为：与这两座城市 直接 相连的道路总数。
如果存在一条道路直接连接这两座城市，则这条道路只计算 一次 。
整个基础设施网络的 最大网络秩 是所有不同城市对中的 最大网络秩 。
给你整数 n 和数组 roads，返回整个基础设施网络的 最大网络秩 。

输入：n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
输出：4
解释：城市 0 和 1 的网络秩是 4，因为共有 4 条道路与城市 0 或 1 相连。位于 0 和 1 之间的道路只计算一次。
"""


class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        res = [0] * n
        for i, j in roads:
            res[i] += 1
            res[j] += 1
        res.sort(reverse=True)
        print(res)
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if [i, j] in roads or [j, i] in roads:
                    temp = res[i] + res[j] - 1
                else:
                    temp = res[i] + res[j]
                if temp > ans:
                    ans = temp
        return ans



if __name__ == '__main__':
    s = Solution()
    # print(s.maximalNetworkRank(n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))
    print(s.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))
