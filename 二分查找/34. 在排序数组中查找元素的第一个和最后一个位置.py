"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 处理target不在nums中的情况
        if target not in nums:
            return [-1, -1]
        # 二分法开始找target首次出现的下标
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + int((high - low) / 2)
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        # 此时low和high均指向第一个target，则low不动，用high寻找最后一个target
        while high < len(nums) - 1:
            if nums[high + 1] == target:
                high += 1
            else:
                break
        return [low, high]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange(nums=[1], target=1))
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
