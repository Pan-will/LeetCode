"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。说明：你的算法应该具有线性时间复杂度。
你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
"""


class Solution(object):
    # 异或运算
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

    # list
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for ch in nums:
            if ch in res:
                res.pop(res.index(ch))
            else:
                res.append(ch)
        return res[0]

    # 字典
    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for ch in nums:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
        for key, value in dict.items():
            if value == 1:
                return key


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([4, 1, 2, 1, 2]))
