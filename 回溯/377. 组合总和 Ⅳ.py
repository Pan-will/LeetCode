"""
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:
nums = [1, 2, 3]
target = 4
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。
因此输出为 7。
"""

# 思路：回溯模板超时。。。
class Solution(object):
    def __init__(self):
        self.res = []

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 特判
        if not nums:
            return []
        # 可以重复调用，所以先排个序，确保相同数字相邻
        nums.sort()
        # 获取元素个数
        n = len(nums)
        # 调用函数
        self.dfs(nums, target, n, 0, 0, [])
        return len(self.res)

    def dfs(self, nums, target, n, begin, temp_sum, temp):
        # 临时和大于target 或者 已遍历完，则不符合
        if temp_sum > target or begin == n:
            return
        # 递归出口：和等于target，则找到新答案
        if temp_sum == target:
            self.res.append(temp)
            return
        for i in range(n):
            if temp_sum + nums[i] > target:
                break
            self.dfs(nums, target, n, i, temp_sum + nums[i], temp + [nums[i]])


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([4, 2, 1], 32))
