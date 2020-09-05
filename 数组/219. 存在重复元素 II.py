"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i + 1, i + k + 1):
                if j < len(nums) and nums[i] == nums[j]:
                    return True
        return False

    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        j = i + 1
        while i < len(nums) and j < len(nums):
            for index in range(j, j + k):
                if index < len(nums) and nums[index] == nums[i]:
                    return True
            i += 1
            j = i + 1
        return False

    # 用字典（dict），set和dict类似，也是一组key的集合，但不存储value, 由于key不能重复
    def containsNearbyDuplicate3(self, nums, k):
        arr = {}
        for i in range(len(nums)):
            if nums[i] in arr and i - arr[nums[i]] <= k:
                return True
            arr[nums[i]] = i
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyDuplicate3(nums=[1, 2, 3, 1], k=3))
