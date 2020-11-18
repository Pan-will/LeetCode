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
        lists = list(S)
        lists.sort()
        n = len(lists)
        visit = [0 for _ in range(n)]
        self.dfs(lists, n, visit, [])
        return self.res

    def dfs(self, string, n, visit, temp):
        # 定义递归出口
        if len(temp) == len(string):
            self.res.append(temp)
            return
        for i in range(n):
            if not visit[i]:
                if i > 0 and visit[i - 1] == 1 and string[i - 1] == string[i]:
                    continue
                visit[i] = 1
                self.dfs(string, n, visit, temp+[string[i]])
                visit[i] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation(S="3z4"))
