"""
根据此前遇到的题目，总结一个回溯法模板代码。
随机应变很重要。
"""


class Solution():
    # 返回值，定义为全局变量
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
            # for循环横向遍历
            for i in range(n):
                # 当且仅当当前字符未被访问
                if not visit[i]:
                    # 用temp记录当前访问
                    temp.append(string[i])
                    visit[i] = 1
                    # 递归调用，纵向遍历
                    self.dfs(string, temp, visit, n)
                    # 回退
                    temp.pop(-1)
                    visit[i] = 0

    # def backtracking(self, 参数列表):
    #     # 定义递归出口
    #     if 终止条件：
    #         保存结果
    #         return
    #     for i in range(n):
    #         处理
    #         self.dfs(参数)
    #         处理回退
