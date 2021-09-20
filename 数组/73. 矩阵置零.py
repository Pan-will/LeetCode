"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""


class Solution(object):
    # 思路：哈希表，key域存下标，value域存（row, column）。
    # 遍历哈希表，取得每一个row和column，遍历将其行列都置为0。
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        mydict = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mydict[i] = (i, j)
        if mydict:
            for item in mydict.values():
                r, c = item[0], item[1]
                # 置行为0
                for i, num in enumerate(matrix[r]):
                    matrix[r][i] = 0
                # 置列为0——注意技巧
                for j in range(len(matrix)):
                    matrix[j][c] = 0


if __name__ == '__main__':
    s = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    for item in matrix:
        print(item)
    s.setZeroes(matrix)
    print(matrix)
