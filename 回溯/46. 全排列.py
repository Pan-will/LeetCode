# coding=utf-8
"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 特判
        if not nums:
            return
        # 取原数组长度
        n = len(nums)
        # 设置访问标记数组，初始值均为0
        visit = [0 for _ in range(n)]
        temp = []
        self.dfs(nums, n, temp, visit)
        return self.res

    def dfs(self, nums, n, temp, visit):
        if len(temp) == len(nums):
            self.res.append(temp)
        else:
            for i in range(n):
                if not visit[i]:
                    visit[i] = 1
                    self.dfs(nums, n, temp+[nums[i]], visit)
                    visit[i] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
