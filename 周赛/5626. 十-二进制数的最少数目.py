"""
如果一个十进制数字不含任何前导零，且每一位上的数字不是 0 就是 1 ，那么该数字就是一个 十-二进制数 。例如，101 和 1100 都是 十-二进制数，而 112 和 3001 不是。

给你一个表示十进制整数的字符串 n ，返回和为 n 的 十-二进制数 的最少数目。

示例 1：

输入：n = "32"
输出：3
解释：10 + 11 + 11 = 32
"""


class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        res = -1
        for digit in n:
            if int(digit) > res:
                res = int(digit)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minPartitions("32"))
