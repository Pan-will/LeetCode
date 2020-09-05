"""
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == "0" or b == "0":
            return a if b == "0" else b
        # 反转
        a = a[::-1]
        b = b[::-1]
        # 保证a串短，以a串为准进行遍历
        if len(a) > len(b):
            a, b = b, a
        # 两串长度统一
        while len(a) < len(b):
            a += "0"
        # print(a, b)
        result = ""
        extra = 0  # 进位
        for index, num in enumerate(a):
            ans = (int(num) + int(b[index]) + extra) % 2
            if int(num) + int(b[index]) + extra > 1:
                extra = 1
            else:
                extra = 0
            result += str(ans)
        # 只用判断最高位有进位，不用判断无进位情况
        if extra == 1:
            result += "1"
        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary2(a="1111", b="1"))
    print(solution.addBinary2(a="10", b="1011"))
