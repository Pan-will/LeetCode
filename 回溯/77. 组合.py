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
    def __init__(self):
        self.res = []

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
        return self.res
    def dfs(self, nums, n, k, begin, temp, res, visit):
        if len(temp) == k: res.append(temp)
        else:
            for i in range(n):
                if visit[i] == 0:
                    visit[i] = 1
                    self.dfs(nums, n, k, begin, temp+[nums[i]], res, visit)
                    visit[i] = 0


    # def dfs(self, nums, n, k, begin, temp):
    #     # 定义递归出口：长度为k
    #     if len(temp) == k:
    #         self.res.append(temp)
    #     for i in range(begin, n):
    #         if len(temp) > k:
    #             break
    #         # 递归
    #         self.dfs(nums, n, k, i + 1, temp + [nums[i]])


if __name__ == '__main__':
    s = Solution()
    print(s.combine(5,3))
