"""
找出所有相加之和为 n 的 k 个数的组合。
组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, 10)]
        sizeN = len(nums)
        self.dfs(nums, sizeN, k, n, 0, 0, [])
        return self.res

    def dfs(self, nums, sizeN, k, n, begin, temp_sum, temp):
        # 定义递归出口，长度为k且和为n
        if len(temp) == k and temp_sum == n:
            self.res.append(temp)
            return
        for i in range(begin, sizeN):
            if temp_sum > n or len(temp) > k:
                break
            self.dfs(nums, sizeN, k, n, i+1, temp_sum+nums[i], temp+[nums[i]])


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(k=3, n=9))
