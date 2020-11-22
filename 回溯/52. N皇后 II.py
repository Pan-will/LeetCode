"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
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
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        queen = [-1] * n
        # column = [-1] * n
        # dia1 = [-1] * (2 * n)
        # dia2 = [-1] * (2 * n)
        column = set()
        dia1 = set()
        dia2 = set()
        self.dfs(n, res, queen, column, dia1, dia2, 0)
        return len(res)

    def dfs(self, n, res, queen, column, dia1, dia2, row):
        if row == n:
            res.append(1)
            return
        for i in range(n):
            if i in column or row - i in dia1 or row + i in dia2:
                continue
            queen[row] = i
            # column[i] = i
            # dia1[row - i] = row-i
            # dia2[row + i] = row+i
            column.add(i)
            dia1.add(row-i)
            dia2.add(row+i)
            self.dfs(n, res, queen, column, dia1, dia2, row + 1)
            queen[row] = -1
            # column[i] = -1
            # dia1[row - i] = -1
            # dia2[row + i] = -1
            column.remove(i)
            dia1.remove(row-i)
            dia2.remove(row+i)


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(4))
