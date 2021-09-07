class Solution:
    def spiralOrder(self, array):
        res = []
        if not array:
            return res
        beginRow = 0
        endRow = len(array) - 1
        beginCol = 0
        endCol = len(array[0]) - 1
        while beginRow <= endRow and beginCol <= endCol:
            for i in range(beginCol, endCol + 1):
                res.append(array[beginRow][i])
            beginRow += 1
            for i in range(beginRow, endRow + 1):
                res.append(array[i][endCol])
            endCol -= 1
            if beginRow <= endRow:
                # range函数是左开右闭的
                for i in range(endCol, beginCol - 1, -1):
                    res.append(array[endRow][i])
                endRow -= 1
            if beginCol <= endCol:
                for i in range(endRow, beginRow - 1, -1):
                    res.append(array[i][beginCol])
                beginCol += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
