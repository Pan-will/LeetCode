class Solution:
    def spiralOrder(self, matrix):
        res = []
        if not matrix:
            return res
        beginRow = 0
        endRow = len(matrix) - 1
        beginCol = 0
        endCol = len(matrix[0]) - 1
        while beginRow <= endRow and beginCol <= endCol:
            for i in range(beginCol, endCol + 1):
                res.append(matrix[beginRow][i])
            beginRow += 1
            for i in range(beginRow, endRow + 1):
                res.append(matrix[i][endCol])
            endCol -= 1
            if beginRow <= endRow:
                # range函数是左开右闭的
                for i in range(endCol, beginCol - 1, -1):
                    res.append(matrix[endRow][i])
                endRow -= 1
            if beginCol <= endCol:
                for i in range(endRow, beginRow - 1, -1):
                    res.append(matrix[i][beginCol])
                beginCol += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
