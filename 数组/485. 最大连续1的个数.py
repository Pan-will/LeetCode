"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

注意：
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

思路：
1、处理好len(nums) < 2时的情形；
2、用指针i遍历nums，用ans[]存放每一串连续1的长度，用计数器count记录：
    i指向的是1则计数器加1；
    i指向的不是1且前一为是1，则将计数器值添加到ans[]中，并清空计数器；
3、返回max(ans)。
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1 if nums[0] == 1 else 0
        ans = []
        if len(nums) == 1:
            ans.append(count)
        for i in range(1, len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i - 1] == 1 and nums[i] != 1:
                ans.append(count)
                count = 0
            if i == len(nums) - 1:
                ans.append(count)
        return max(ans)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(solution.findMaxConsecutiveOnes([1]))
