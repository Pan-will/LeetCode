"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
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
                    # 跳过重复元素
                    if i > 0 and visit[i - 1] == 1 and nums[i] == nums[i - 1]:
                        continue
                    # 访问标记数组，将当前元素设为已标记
                    visit[i] = 1
                    self.dfs(nums, n, temp + [nums[i]], visit)
                    # 回退
                    visit[i] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1]))
