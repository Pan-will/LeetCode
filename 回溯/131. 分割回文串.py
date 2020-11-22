"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def __init__(self):
        # 返回值，定义为全局变量
        self.res = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        n = len(s)
        stack = []
        self.dfs(s, n, stack, 0)
        return self.res

    def dfs(self, string, n, stack, begin):
        if begin == n:
            self.res.append(stack)
            return
        for i in range(begin, n):
            if not self.isPalindrome(string[begin: i + 1]):
                continue
            self.dfs(string, n, stack+[string[begin: i + 1]], i + 1)

    # 判断串是否回文
    def isPalindrome(self, string):
        return string == string[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aba"))
