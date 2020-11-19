"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.dfs(n, n, n, [])
        return self.res

    def dfs(self, left, right, n, temp):
        if len(temp) == 2 * n:
            self.res.append("".join(temp))
            return
        if left > 0:
            temp.append("(")
            self.dfs(left - 1, right, n, temp)
            temp.pop()
        if right > 0 and right > left:
            temp.append(")")
            self.dfs(left, right - 1, n, temp)
            temp.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
