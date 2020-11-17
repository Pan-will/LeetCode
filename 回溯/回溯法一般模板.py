"""
根据此前遇到的题目，总结一个回溯法模板代码。
随机应变很重要。
"""


class Solution():
    def __init__(self):
        self.res = []

    def function(self, string):
        n = len(string)
        temp = []
        visit = [0 for _ in range(n)]
        self.dfs(string, temp, visit, n)
        return self.res

    def dfs(self, string, temp, visit, n):
        # 定义递归出口
        if len(temp) == len(string):
            self.res.append("".join(temp))
        else:
            for i in range(n):
                # 当且仅当当前字符未被访问
                if not visit[i]:
                    # 凑temp
                    temp.append(string[i])
                    visit[i] = 1
                    # 递归调用
                    self.dfs(string, temp, visit, n)
                    # 回退
                    temp.pop(-1)
                    visit[i] = 0
