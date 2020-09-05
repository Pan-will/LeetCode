"""
接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，返回新的字符串。

示例 1：
输入: "Hello"
输出: "hello"
"""


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for i, ch in enumerate(str):
            if ord(ch) <= 90 and ord(ch) >= 65:
                res += chr(ord(ch) + 32)
            else:
                res += ch
        return res

    def toLowerCase2(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


if __name__ == '__main__':
    solution = Solution()
    print(solution.toLowerCase("HellOKDAKGRGMAkrewajkE"))
