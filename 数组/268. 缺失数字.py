"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(solution.missingNumber([0]))
