"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

思路：折半查找，关键在于停止循环的条件。
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)

        i, j = 0, len(nums) - 1
        while i < j-1:
            if target == nums[i]:
                return i
            elif target == nums[j]:
                return j
            # 折半查找
            temp = int((i + j) / 2)
            if target == nums[temp]:
                return temp
            elif target > nums[temp]:
                i = temp
            elif target < nums[temp]:
                j = temp
        if target == nums[i]:
            return i
        else:
            return i + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1], 1))
