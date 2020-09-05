# encoding=utf-8
"""
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。
请你设计一种算法，将图像旋转 90 度。
不占用额外内存空间能否做到？

示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""


class Solution(object):
    # 思路：先转置，然后每行前后对调。
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        hang = len(matrix)
        lie = len(matrix[0])
        # 转置
        for i in range(hang):
            for j in range(i, lie):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # 每行前后对调
        for k in range(hang):
            matrix[k] = matrix[k][::-1]
        return matrix

    def rotate2(self, matrix):
        matrix[::] = zip(*matrix[::-1])
        return matrix


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotate2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
