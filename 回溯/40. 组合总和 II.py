"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 特判
        if not candidates:
            return []
        candidates.sort()
        # 获取元素个数
        n = len(candidates)
        # 调用函数
        self.dfs(candidates, target, n, 0, 0, [])
        return self.res

    def dfs(self, candidates, target, n, begin, temp_sum, temp):
        if temp_sum == target:
            self.res.append(temp)
            return
        for i in range(begin, n):
            # 超过目标值了，不符合
            if temp_sum + candidates[i] > target:
                break
            # 不能选相同的元素
            if i > begin and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target, n, i+1, temp_sum + candidates[i], temp + [candidates[i]])


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
