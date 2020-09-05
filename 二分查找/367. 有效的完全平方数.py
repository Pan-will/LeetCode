"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
说明：不要使用任何内置的库函数，如  sqrt。

示例 1：
输入：16
输出：True

示例 2：
输入：14
输出：False
"""


class Solution(object):
    # 思路：利用 1+3+5+7+9+…+(2n-1)=n^2=num，即完全平方数肯定是前n个连续奇数的和
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        ans = 0
        for i in range(1, num, 2):
            ans += i
            if ans == num:
                return True
        return False

    # 二分法
    def isPerfectSquare2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        i, j = 2, int(num / 2)
        while i <= j:
            mid = int((i + j) / 2)
            if mid * mid == num:
                return True
            elif mid * mid > num:
                j = mid - 1
            else:
                i = mid + 1
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPerfectSquare2(16))
