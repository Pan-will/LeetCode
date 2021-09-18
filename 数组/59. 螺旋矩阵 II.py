"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，
且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return [[1]]
        # 定义方向向量
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        x, y = 0, 0  # 当前位置
        extra = 0  # 偏移量
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n * n):
            matrix[x][y] = i + 1
            a = x + dx[extra]
            b = y + dy[extra]
            if a < 0 or a == n or b < 0 or b == n or matrix[a][b] != 0:
                extra = (extra + 1) % 4
                a = x + dx[extra]
                b = y + dy[extra]
            x = a
            y = b
        return matrix


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
