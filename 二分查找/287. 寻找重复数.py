# coding=utf-8
"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
理解：即nums长为n+1，里面的元素值范围：[1,n]，有且仅有一个重复值。
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3
"""


# 题意：即nums长为n+1，里面的元素值范围：[1,n]，有且仅有一个重复值，但该值可以重复多次，
# 所以[1,n]有的数可以不在nums里。
class Solution(object):
    # 二分查找
    def findDuplicate(self, nums):
        low = 1
        high = len(nums) - 1
        while low < high:
            mid = low + int((high - low) / 2)
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low

    # 双指针
    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        low, fast = 0, 1
        while fast < len(nums):
            if nums[low] != nums[fast]:
                low += 1
                fast += 1
            else:
                return nums[fast]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findDuplicate([1, 1]))
    print(solution.findDuplicate([7, 9, 7, 4, 2, 8, 7, 7, 1, 5]))
