"""
给定两个整数，被除数 dividend 和除数 divisor。
将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分。
例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

eg：11÷3

∵11>3

∴res>=1

又∵11>3+3=6

∴res>=2 (1+1)

又∵11<6+6=12

∴res<4 (2+2)

即2<=res<4

递归部分：

又11-6=5>3

∴restemp >= 1

又∵5<6 (3+3)

∴restemp<2 (1+1)

即1<=restemp<2

又∵5-3=2<3

∴restemp = 1

返回:

∴res = 2 + restemp = 2+1=3
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        # 符号
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        # 溢出的情况
        if abs(divisor) == 1:
            if abs(dividend) > 2 ** 31 - 1:
                return 2 ** 31 - 1 if sign > 0 else -2 ** 31
        tema = abs(dividend)
        temb = abs(divisor)
        res = self.DiGuiDiv(tema, temb)
        return res if sign > 0 else -res

    def DiGuiDiv(self, a, b):
        if a < b:
            return 0
        count = 1
        temp = b
        while (temp + temp) <= a:
            count += count
            temp += temp
        return count + self.DiGuiDiv(a - temp, b)


if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(-2147483648, -1))
