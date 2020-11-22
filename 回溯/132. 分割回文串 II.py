"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回符合要求的最少分割次数。

示例:
输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        res = []
        stack = []
        self.dfs(s, n, res, stack, 0)
        return min(res)-1

    def dfs(self, string, n, res, stack, begin):
        if begin == n:
            res.append(len(stack))
            return
        for i in range(begin, n):
            if not self.isPalindrome(string, begin, i):
                continue
            self.dfs(string, n, res, stack + [string[begin:i + 1]], i + 1)

    def isPalindrome(self, string, begin, end):
        while begin < end:
            if string[begin] != string[end]:
                return False
            begin += 1
            end -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.minCut("abb"))
