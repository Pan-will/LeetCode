"""
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:
 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]

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

    # 要得到3个a、2个c和1个b的全排列，你首先需要选择一个起始字符：a、b或c。如果是a，那么你需要2个a、2个c和1个b的全排列。
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # 取得原串的长度
        n = len(S)
        # py中string不能修改，先list化，然后排序，确保相同字符相邻
        Str = list(S)
        Str.sort()
        # 初始化访问标记数组visit
        visit = [0 for _ in range(n)]
        # 设置一个空串，暂存当前组合串，作为实参
        temp = []
        # 调用函数
        self.dfs(Str, temp, n, visit)
        return self.res

    def dfs(self, Str, temp, n, visit):
        # 设置递归出口，临时串长度和原串相等，则一个新答案诞生
        if len(temp) == len(Str):
            self.res.append("".join(temp))
        # 否则，遍历字符串，选择合适的字符来拼凑temp，知道符合出口条件
        else:
            for i in range(n):
                # 访问当前字符的前提：当前字符还未被访问到
                if not visit[i]:
                    # 忽略相同的字符，这就是调用前先sort的目的
                    if i > 0 and visit[i - 1] == 1 and Str[i - 1] == Str[i]:
                        continue
                    # 将当前字符拼凑到temp中
                    temp.append(Str[i])
                    # 修改标记数组
                    visit[i] = 1
                    # 递归调用
                    self.dfs(Str, temp, n, visit)
                    # 回退到上一步
                    temp.pop(-1)
                    # 同样，标记数组也要回退
                    visit[i] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.permutation("abba"))
