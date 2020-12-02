"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:
输入:
nums1 = [3, 4, 6, 5],nums2 = [9, 1, 2, 5, 8, 3],k = 5
输出:
[9, 8, 6, 5, 3]

示例 2:
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
"""


# 题目要求保留数字原序
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        size1 = len(nums1)
        size2 = len(nums2)
        res = [0] * k
        begin, end = max(0, k - size2), min(k, size1)
        print("打印begin和end：", begin, end)

        for i in range(begin, end + 1):
            # 分别从两个数组中得到指定长度的最大子序列
            sub1 = self.findMax(nums1, i)
            sub2 = self.findMax(nums2, k - i)
            print("第", i, "轮循环，两个最大子序列分别是：", sub1, sub2)
            # 将两个最大子序列合并
            tempMerge = self.merge(sub1, sub2)
            if self.compare(tempMerge, res, 0, 0) > 0:
                res = tempMerge
        return res

    # 将两个序列合并成一个序列，要求结果是最大序列
    def merge(self, suba, subb):
        l1, l2 = len(suba), len(subb)
        if not l1:
            return subb
        if not l2:
            return suba
        mergeSize = l1 + l2
        res = []
        i, j = 0, 0
        for _ in range(mergeSize):
            if self.compare(suba, subb, i, j) > 0:
                res.append(suba[i])
                i += 1
            else:
                res.append(subb[j])
                j += 1
        return res

    def compare(self, suba, subb, i, j):
        l1, l2 = len(suba), len(subb)
        while i < l1 and j < l2:
            diff = suba[i] - subb[j]
            if diff:
                return diff
            i += 1
            j += 1
        return (l1 - i) - (l2 - j)

    # 从给定数组中找出k个数字拼成最大数，保持数字原序
    def findMaxdigit(self, nums, k):
        # 初始化栈
        stack = []
        # 从左往右遍历，保证字典序
        for i, digit in enumerate(nums):
            # 当剩余未遍历到的数字足够凑齐k个数字，且栈顶元素大于当前数字时：才出栈。
            while len(nums) - i > k - len(stack) + 1 and stack[-1] < digit:
                stack.pop(-1)
            # 栈中元素不够k个或者栈顶元素小于当前数字，直接入栈
            stack.append(digit)
        # 去掉多余数字，除了开始的-1，只要k个元素
        while len(stack) > k + 1:
            stack.pop(-1)
        if len(nums) <= k:
            return nums
        # 返回时抹去前导的-1，只要后面k个数字
        else:
            return stack[-k:]

    def findMax(self, nums, k):
        stack = [0] * k
        length = len(nums)
        top = -1
        remain = length - k
        for i,num in enumerate(nums):
            while top >= 0 and stack[top] < num and remain > 0:
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1
        return stack


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxdigit([6, 0, 4], 2))
    # print(s.maxNumber([6, 7], [6, 0, 4], 5))
    # print(s.maxNumber(nums2=[3, 4, 6, 5], nums1=[9, 1, 2, 5, 8, 3], k=5))
