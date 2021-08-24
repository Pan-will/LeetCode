"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。


示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 特判
        if len(nums) < 2: return True
        # 初值
        road = nums[0]
        cur = nums[0]
        index = 0
        # 直到跳过了或者刚好够数就停下
        while road <= len(nums) and index <= len(nums):
            road += cur
            if road > len(nums):
                return False
            elif road == len(nums):
                return True
            cur = nums[index + cur]
            index += cur
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 0, 4]))
