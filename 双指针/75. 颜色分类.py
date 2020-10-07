"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
"""


class Solution(object):
    # 思路：双指针
    # i和j分别从头尾遍历，i收集0，j收集2。
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        index = 0
        while index <= j:
            while index <= j and nums[index] == 2:
                nums[index], nums[j] = nums[j], nums[index]
                j -= 1
            if nums[index] == 0:
                nums[index], nums[i] = nums[i], nums[index]
                i += 1
            index += 1
        print(nums)

    # sort()也蛮香。
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()


if __name__ == '__main__':
    s = Solution()
    s.sortColors([1, 2, 0])
