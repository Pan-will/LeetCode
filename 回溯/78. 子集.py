"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        self.dfs(nums, n, 0, [])
        return self.res

    def dfs(self, nums, n, begin, temp):
        self.res.append(temp)
        for i in range(begin, n):
            self.dfs(nums, n, i + 1, temp + [nums[i]])




if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
