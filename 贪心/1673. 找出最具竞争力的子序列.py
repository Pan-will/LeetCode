"""
给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。

数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。

在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 。
例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。
 

示例 1：
输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。

示例 2：
输入：nums = [2,4,3,3,5,4,9,6], k = 4
输出：[2,3,3,4]
"""


# 思路：贪心算法 + 栈
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 初始化栈
        stack = [-1]
        # 从左往右遍历，保证字典序
        for i, digit in enumerate(nums):
            # 当剩余未遍历到的数字足够凑齐k个数字，且栈顶元素大于当前数字时：才出栈。
            while len(nums) - i > k-len(stack)+1 and stack[-1] > digit:
                stack.pop(-1)
            # 栈中元素不够k个或者栈顶元素小于当前数字，直接入栈
            stack.append(digit)
        # 去掉多余数字，除了开始的-1，只要k个元素
        while len(stack) > k+1:
            stack.pop(-1)
        # 返回时抹去前导的-1，只要后面k个数字
        return stack[-k:]


if __name__ == '__main__':
    s = Solution()
    # print(s.mostCompetitive(nums=[3, 5, 2, 6], k=2))
    # print(s.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))
    print(s.mostCompetitive([71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2], 3))
