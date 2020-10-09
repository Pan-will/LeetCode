"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
示例 1:
输入: 1
输出: true
解释: 20 = 1
"""
import math


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 特判
        if n == 0:
            return False
        while n % 2 == 0:
            n = n // 2
        return n == 1


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(12))
    print(s.isPowerOfTwo(0))
    print(s.isPowerOfTwo(3))
    print(s.isPowerOfTwo(8))
