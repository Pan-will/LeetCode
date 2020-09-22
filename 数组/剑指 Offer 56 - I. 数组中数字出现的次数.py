"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
"""


class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        # 特判：处理第一个和最后一个元素
        if nums[0] != nums[1]:
            res.append(nums[0])
        if nums[-1] != nums[-2]:
            res.append(nums[-1])
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i - 1] or nums[i] == nums[i + 1]:
                continue
            else:
                res.append(nums[i])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumbers(nums=[4, 1, 4, 6]))
