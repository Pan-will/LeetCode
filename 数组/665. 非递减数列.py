"""
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
 
示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        # 计数器
        flag = 0
        for i in range(1, len(nums)):
            # 先检验是否已经修改过两次及以上
            if flag >= 2:
                return False
            # 当前元素满足非递减，则看下一个元素
            if nums[i - 1] <= nums[i]:
                continue
            # 不满足非递减，需要修改，标志符加1
            flag += 1
            if i >= 2 and nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1]
            else:
                nums[i - 1] = nums[i]
        return flag <= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPossibility(nums=[4, 1, 3, 2, 4, 5]))
