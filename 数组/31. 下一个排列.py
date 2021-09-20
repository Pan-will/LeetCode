"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]
"""


class Solution(object):
    # 思路：
    # 若已是降序排列，则返回升序序列；
    # 从右往左遍历找到第一个顺序对，即nuns[i]<a[i+1]，记录a[i]即值较小数；
    # 再次从右往左遍历，找到第一个大于a[i]的数：a[j]。
    # 交换a[i]和a[j]，并将[i:]区间升序。
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2]
    nums2 = [2, 3, 1]
    nums3 = [1, 5, 1]
    s.nextPermutation(nums1)
    s.nextPermutation(nums2)
    s.nextPermutation(nums3)
    print(nums1, nums2, nums3)
