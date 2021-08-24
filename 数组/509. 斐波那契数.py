"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。
该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 

示例 1：
输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.

示例 2：
输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
"""


class Solution(object):
    # 迭代
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fibs = []
        fibs.append(0)
        fibs.append(1)
        if N <= 1:
            return fibs[N]
        for i in range(2, N + 1):
            fibs.append(fibs[i - 2] + fibs[i - 1])
        return fibs[-1]

    # 递归
    def fib_dg(self, n):
        if n < 2: return n
        return self.fib_dg(n-1) + self.fib_dg(n-2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(31))
    print(solution.fib_dg(31))
