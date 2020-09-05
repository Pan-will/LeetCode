"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k % len(nums):] + nums[0:-k % len(nums)]

        return nums

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = (nums[0:-k][::-1] + nums[k + 1:][::-1])[::-1]

        return nums

    def rotate3(self, nums, k):
        nums[:] = (nums[i] for i in range(-(k % len(nums)), len(nums) - k % len(nums)))
        return nums

    def rotate4(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotate4([1, 2, 3, 4, 5, 6, 7], 3))
