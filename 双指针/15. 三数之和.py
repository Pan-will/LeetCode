"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    # 暴力法：两层循环找遍所有情况
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                other = 0 - nums[i] - nums[j]
                temp = [nums[i], nums[j], other]
                if other in nums[j + 1:] and temp not in res:
                    res.append(temp)
        return res

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for k in range(len(nums)):
            i, j = k + 1, len(nums) - 1
            while i < j:
                temp = [nums[k], nums[i], nums[j]]
                if nums[i] + nums[j] == -nums[k] and temp not in res:
                    res.append(temp)
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] > -nums[k]:
                    j -= 1
                else:
                    i += 1
        return res

    def threeSum3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            tar = 0 - nums[k]
            i, j = k + 1, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] > tar:
                    j -= 1
                elif nums[i] + nums[j] < tar:
                    i += 1
                else:
                    temp = [nums[k], nums[i], nums[j]]
                    if temp not in res:
                        res.append([nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum3(nums=[-1, 0, 1, 2, -1, -4]))
