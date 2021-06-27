"""
给你一个字符串 num ，表示一个大整数。
请你在字符串 num 的所有 非空子字符串 中找出 值最大的奇数 ，并以字符串形式返回。
如果不存在奇数，则返回一个空字符串 "" 。

子字符串 是字符串中的一个连续的字符序列。


示例 1：
输入：num = "52"
输出："5"
解释：非空子字符串仅有 "5"、"2" 和 "52" 。"5" 是其中唯一的奇数。
"""


class Solution(object):
    # 去掉字符串前面的无效0
    def myFormat(self, arr):
        for i, ch in enumerate(arr):
            if ch != "0":
                return arr[i:]
        return ""

    # 判断两个字符串表示的数哪个大，返回较大者
    def judge(self, str1, str2):
        # 去掉字符串前面的无效0
        str1 = self.myFormat(str1)
        str2 = self.myFormat(str2)
        # 若两字符串某个为空 或 长度不一样
        if not str1 or len(str2) > len(str1): return str2
        if not str2 or len(str1) > len(str2): return str1
        if str1 == str2: return str1
        # 若两字符串长度一样
        for i, ch in enumerate(str1):
            if int(str1[i]) > int(str2[i]):
                return str1
            elif int(str1[i]) < int(str2[i]):
                return str2

    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # 判空
        if not num:
            return ""
        # 本身就是奇数
        if int(num[-1]) % 2 == 1:
            return num
        res = ""
        for i, ch in enumerate(num):
            if int(ch) % 2 == 1:
                res = self.judge(res, num[:i + 1])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.largestOddNumber("526957"))
