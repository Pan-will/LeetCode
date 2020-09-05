"""
给定一个大小为 n 的数组，找到其中的多数元素。
多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 转set去重
        setnum = set(nums)
        for i in setnum:
            if nums.count(i) > int(len(nums) / 2):
                return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))
