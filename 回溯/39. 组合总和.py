"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
 
示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 特判
        if not candidates:
            return []
        # 可以重复调用，所以先排个序，确保相同数字相邻
        candidates.sort()
        # 获取元素个数
        n = len(candidates)
        # 调用函数
        self.dfs(candidates, target, n, 0, 0, [])
        return self.res

    def dfs(self, candidates, target, n, begin, temp_sum, temp):
        if temp_sum > target or begin == n:
            return
        if temp_sum == target:
            self.res.append(temp)
            return
        for i in range(begin, n):
            if temp_sum + candidates[i] > target:
                break
            self.dfs(candidates, target, n, i, temp_sum + candidates[i], temp + [candidates[i]])


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum(candidates=[2, 3, 5], target=8))
