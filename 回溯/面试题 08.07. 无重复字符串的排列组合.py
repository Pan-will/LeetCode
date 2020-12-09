"""
无重复字符串的排列组合。
编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:
 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]

示例2:
 输入：S = "ab"
 输出：["ab", "ba"]

提示:
字符都是英文字母。
字符串长度在[1, 9]之间。
"""


class Solution(object):
    def __init__(self):
        # res作为返回值，设为全局变量
        self.res = []

    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # 获取原串的长度
        n = len(S)
        # 暂存此趟循环的组合串
        temp = []
        # 初始化访问标记数组
        visit = [0 for _ in range(n)]
        # 调用函数
        self.dfs(S, temp, visit, n)
        return self.res

    def dfs(self, Str, temp, visit, n):
        # 定义递归出口：temp长度与原串相等，则一个新的答案诞生
        if len(Str) == len(temp) and "".join(temp) not in self.res:
            self.res.append("".join(temp))
            return
        # 否则，遍历原串，逐个取得字符拼凑temp
        else:
            for i in range(n):
                # 当且仅当当前字符未被访问过
                if not visit[i]:
                    # 取得字符拼凑temp
                    temp.append(Str[i])
                    # 修改访问标记数组
                    visit[i] = 1
                    # 递归
                    self.dfs(Str, temp, visit, n)
                    # 回退
                    temp.pop(-1)
                    # 标记数组也要回退
                    visit[i] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.permutation("aab"))
