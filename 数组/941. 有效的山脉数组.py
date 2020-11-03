"""
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

示例 1：
输入：[3,5,5]
输出：false

示例 2：
输入：[0,3,2,1]
输出：true
"""


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        i = 0
        # 找上坡
        while i+1 < n and A[i] < A[i + 1]:
            i += 1
        # 整个数组不能是单调的
        if i == 0 or i == n - 1:
            return False
        # 找下坡
        while i+1 < n and A[i] > A[i + 1]:
            i += 1
        return i == n - 1


if __name__ == '__main__':
    s = Solution()
    print(s.validMountainArray([0, 3, 2, 1]))
