# -*- coding: utf-8 -*
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, n + 1)]
        temp = []
        res = []
        visit = [0 for _ in range(n)]
        self.dfs(nums, n, k, 0, temp, res, visit)
        return res

    def dfs(self, nums, n, k, begin, temp, res, visit):
        if len(temp) == k:
            res.append(temp)
        else:
            for i in range(n):
                if visit[i] == 0:
                    visit[i] = 1
                    self.dfs(nums, n, k, begin, temp + [nums[i]], res, visit)
                    visit[i] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.combine(5, 3))
