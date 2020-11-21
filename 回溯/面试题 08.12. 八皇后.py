"""
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。
这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

注意：本题相对原题做了扩展

示例:
 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 返回值
        res = []
        # 皇后
        queens = [-1] * n
        # 列
        columns = set()
        # 主对角线方向
        dia1 = set()
        # 次对角线方向
        dia2 = set()
        self.helper(queens, columns, dia1, dia2, res, n, 0)
        return res

    def helper(self, queens, columns, dia1, dia2, res, n, row):
        if row == n:
            path = self.drawPath(queens, n)
            res.append(path)
        else:
            for i in range(n):
                # if columns[i]: continue
                # d1 = row - i + n - 1
                # if dia1[d1]: continue
                # d2 = row + i
                # if dia2[d2]: continue
                if i in columns or row - i in dia1 or row + i in dia2:
                    continue
                queens[row] = i
                columns.add(i)
                dia1.add(row-i)
                dia2.add(row+i)
                # 递归
                self.helper(queens, columns, dia1, dia2, res, n, row + 1)
                # 回退
                columns.remove(i)
                dia1.remove(row-i)
                dia2.remove(row+i)

    def drawPath(self, queens, n):
        board = []
        row = ["."] * n
        for i in range(n):
            row[queens[i]] = "Q"
            board.append("".join(row))
            row[queens[i]] = "."
        return board


""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""只能保证不在同行、同列"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""


# 只能保证不在同行、同列
def solveNQueens2(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    res = []
    # 调用函数，实参分别是n和存放当前皇后所在列的数组
    self.dfs(n, [], res)
    return res


def dfs(self, n, temp, res):
    # 递归出口：当前路径长度为n，说明找到一个新方案
    if len(temp) == n:
        # 将新方案绘制成棋盘添加到res中并返回
        res.append(self.drawAns(temp))
        return
    # 遍历各列
    for i in range(n):
        # 若当前列未在当前数组中，且对角线上没有皇后
        if i not in temp and self.isLawful(temp, i):
            temp.append(i)
            self.dfs(n, temp, res)
            temp.pop()


# 判断当前位置的对角线上是否有皇后
def isLawful(self, path, k):
    for i in range(len(path)):
        if abs(path[i] - i) == abs(len(path) - k):
            return False
    return True


def drawAns(self, path):
    # print("接下来要画的原始棋盘是：", path)
    ans = []
    temp = [["."] * len(path) for _ in range(len(path))]
    # print("初始化的棋盘是：", temp)
    for i in range(len(path)):
        temp[i][path[i]] = "Q"
    for item in temp:
        ans.append("".join(item))
    # print("规划好的棋盘是：", ans)
    return ans


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
