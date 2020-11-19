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
        nums = [i for i in range(1, n+1)]
        sizeN = len(nums)
        self.dfs(nums, sizeN, k, 0, [])
        return self.res

    def dfs(self, nums, sizeN, k, begin, temp):
        # 定义递归出口：长度为k
        if len(temp) == k:
            self.res.append(temp)
        for i in range(begin, sizeN):
            if len(temp) > k:
                break
            self.dfs(nums, sizeN, k, i+1, temp+[nums[i]])


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
