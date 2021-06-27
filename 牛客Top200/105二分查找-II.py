"""
请实现有重复数字的升序数组的二分查找
给定一个 元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的第一个出现的target，如果目标值存在返回下标，否则返回 -1
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self, nums, target):
        # write code here
        if not nums:
            return -1
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if target > nums[mid]:
                i = mid + 1
            elif target < nums[mid]:
                j = mid - 1
            else:
                while mid != 0 and nums[mid] == nums[mid - 1]:
                    mid -= 1
                return mid
        return -1

    def search2(self, nums, target):
        # write code here
        if not nums:
            return -1
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if target > nums[mid]:
                i = mid + 1
            else:
                j = mid
        return i if nums[i] == target else -1
