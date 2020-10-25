"""
给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。
如果不存在这样的子字符串，返回 -1 。

子字符串 是字符串中的一个连续字符序列
"""


class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -2
        mylist = list(s)
        for i, item in enumerate(mylist):
            if item in mylist[:i]:
                if res < i - s.index(item) - 1:
                    res = i - s.index(item) - 1
        return res if res != -2 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.maxLengthBetweenEqualCharacters(s="aa"))
