"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:
输入: "Hello, my name is John"
输出: 5
"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.split()) == 0:
            return 0
        # 设置计数器，初始值为1
        index = 0
        # 遍历字符串，如果当前遇到的字符是字母前一个字符是空格时，计数器增1
        # 当然，字符串第一个字符单独考虑
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i].isalnum():
                index += 1
        return index

    def countSegments2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 设置计数器，初始值为1
        index = 1
        # 遍历字符串，如果当前遇到的字符不是字母，那么在遇到下一个字母时，计数器增1
        for i in range(len(s)):
            if not s[i - 1].isalnum() and s[i].isalnum():
                index += 1
        return index

    def countSegments3(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 测试用例每个单词后都会有一个空格
        return len(s.split())


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSegments(", , , ,        a, eaefa"))
    print(solution.countSegments("Of all the gin joints in all the towns in all the world,   "))
    print(solution.countSegments("Hello, my, name, is, John"))
    print(solution.countSegments("love live! mu'sic forever"))
