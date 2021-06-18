"""
数值（按顺序）可以分成以下几个部分：
若干空格
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
若干空格

小数（按顺序）可以分成以下几个部分：
（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：
（可选）一个符号字符（'+' 或 '-'）
至少一位数字

部分数值列举如下：
["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：
["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 判空
        if not s or (len(s) == 1 and (s[0] == "+" or s[0] == "-")):
            return False
        # 处理字符串头部的空格
        for i, ch in enumerate(s):
            if ch != " ":
                s = s[i:]
                break
        isDigit = False
        isDot = False
        isE = False
        isSymbol = False
        for i, ch in enumerate(s):
            if ch == " ":  # 串内空格直接跳过
                continue
            # 如果当前字符c是数字：将hasNum置为true；
            # index往后移动一直到非数字或遍历到末尾位置；
            # 如果已遍历到末尾(index == n)，结束循环
            elif ch.isdigit():
                isDigit = True
            elif (ch == "e" or ch == "E") and not isE and isDigit:
                isE = True
                isDigit = False
                isDot = False
                isSymbol = False
            elif (ch == "+" or ch == "-") and not isSymbol and not isDot and not isDigit:
                isSymbol = True
            elif ch == "." and not isDot and not isE:
                isDot = True
            else:
                return False
        return isDigit


if __name__ == '__main__':
    s = Solution()
    print(s.isNumber("   -1E -16"))
    print(s.isNumber("  + -5"))
    print(s.isNumber("1 "))
