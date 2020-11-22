class Solution():
    def solveNQueens(self, n):
        res = []
        queen = [-1] * n
        column = set()
        dia1 = set()
        dia2 = set()
        self.dfs(n, res, queen, column, dia1, dia2, 0)
        return res

    def dfs(self, n, res, queen, column, dia1, dia2, row):
        if row == n:
            path = self.drawPath(queen, n)
            res.append(path)
        for i in range(n):
            if i in column or row - i in dia1 or row + i in dia2:
                continue
            queen[row] = i
            column.add(i)
            dia1.add(row - i)
            dia2.add(row + i)
            self.dfs(n, res, queen, column, dia1, dia2, row + 1)
            queen[row] = -1
            column.remove(i)
            dia1.remove(row - i)
            dia2.remove(row + i)

    def drawPath(self, queen, n):
        ans = []
        tmp = ["."] * n
        for i in range(n):
            tmp[queen[i]] = "Q"
            ans.append("".join(tmp))
            tmp[queen[i]] = "."
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
