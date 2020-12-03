"""
统计所有小于非负整数 n 的质数的数量。

示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""

from math import sqrt


class Solution(object):

    # 题意是统计[2, n]  中质数的个数
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        # 初始化标记数组，假设都是质数
        isPrim = [True] * n
        isPrim[0] = False
        res = 0
        for i in range(2, n):
            if isPrim[i]:
                res += 1
                for j in range(i * i, n, i):
                    isPrim[j] = False
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))
