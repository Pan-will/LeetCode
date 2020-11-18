"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        self.dfs(nums, n, 0, [])
        return self.res

    def dfs(self, nums, n, begin, temp):
        if temp not in self.res:
            self.res.append(temp)
        for i in range(begin, n):
            if i > begin and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, n, i + 1, temp + [nums[i]])


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))
