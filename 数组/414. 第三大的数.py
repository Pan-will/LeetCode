"""
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:
输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.

示例 2:
输入: [1, 2]
输出: 2
解释: 第三大的数不存在, 所以返回最大的数 2 .
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 转set去重
        s = set(nums)
        # 在转回list
        # nums = list(s)
        # 降序排
        # nums.sort(reverse=True)
        # sorted()函数排序后返回的是list类型
        nums = sorted(s, reverse=True)
        if len(s) < 3:
            return nums[0]
        else:
            return nums[2]

    def thirdMax2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 升序排
        nums.sort()
        index = 1
        # 暂存nums最后一个元素
        temp = nums[-1]
        # 从倒数第二个元素倒序遍历
        for j in range(len(nums) - 2, -1, -1):
            if index == 3:
                return temp
            if nums[j] == temp:
                nums.pop(j)
            else:
                temp = nums[j]
                index += 1
        if index != 3:
            return nums[-1]
        else:
            return temp


if __name__ == '__main__':
    solution = Solution()
    print(solution.thirdMax([1, 2]))
    print(solution.thirdMax([1, 5, 2]))
