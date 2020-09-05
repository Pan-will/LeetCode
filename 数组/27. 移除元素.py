"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # 双指针
        i, j = 0, len(nums) - 1
        while i < j:
            # j指向的等于val，j前移
            if nums[j] == val:
                j -= 1
                continue
            # 如果i指向的等于val，交换i和j的值，j前移
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            # i每一趟都后移
            i += 1
        print(nums, i, j)
        if nums[i] == val:
            return len(nums[:i])
        else:
            return len(nums[:i]) + 1

    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] != val:
                i += 1
            elif nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if nums[i] == val:
            return len(nums[:i])
        else:
            return len(nums[:i]) + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement(nums=[0, 1, 2, 2, 3, 2, 4, 2, 5], val=2))
    print(solution.removeElement(nums=[], val=5))
