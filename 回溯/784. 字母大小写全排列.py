"""
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。
返回所有可能得到的字符串集合。

 

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]
 
提示：
S 的长度不超过12。
S 仅由数字和字母组成。
"""


# 原串里有数字、也有字母，所以每选一个字符要加以判断，要是字母则有两种选择，数字就一种。
class Solution(object):
    def __init__(self):
        self.res = []

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # 特判
        if not S:
            return []
        # 将字符串转成list类型
        lists = list(S)
        # 去原串长度
        n = len(lists)
        self.dfs(lists, 0, n, [])
        return self.res

    def dfs(self, string, cur, n, temp):
        # 定义递归出口
        if len(temp) == len(string):
            self.res.append("".join(temp))
            return
        # 数字直接加
        if string[cur].isdigit():
            self.dfs(string, cur + 1, n, temp + [string[cur]])
        # 小写字母
        elif string[cur].islower():
            self.dfs(string, cur + 1, n, temp + [string[cur]])
            self.dfs(string, cur + 1, n, temp + [string[cur].upper()])
        # 大写字母
        elif string[cur].isupper():
            self.dfs(string, cur + 1, n, temp + [string[cur]])
            self.dfs(string, cur + 1, n, temp + [string[cur].lower()])


if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation(S="a1b2"))
