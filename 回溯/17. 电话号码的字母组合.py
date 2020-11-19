"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def __init__(self):
        self.res = []
        self.mydict = {1: [], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
                       4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                       7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 将数字串转成list类型
        nums = list(digits)
        # 获取原串长度，返回值中的每一个串都是这个长度，用于定义递归出口
        n = len(digits)




    def dfs(self, string, n, visit, temp):
        """
        :temp
        :string
        :n
        :visit
        :rtype
        """


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
