"""
包含整数的二维矩阵 M 表示一个图片的灰度。
你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，
平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:
输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # padding：在原矩阵周围加上一圈非有效数字：-10，便于处理边缘元素
        m = len(M[0])
        N = [[-10] + i + [-10] for i in M]
        N = [[-10] * (m + 2)] + N + [[-10] * (m + 2)]
        for i in range(1, len(N) - 1):
            for j in range(1, len(N[0]) - 1):
                # 当前元素及其周围的八个元素：九宫格
                total = [N[i - 1][j - 1], N[i - 1][j], N[i - 1][j + 1], N[i][j - 1], N[i][j], N[i][j + 1],
                         N[i + 1][j - 1], N[i + 1][j], N[i + 1][j + 1]]
                # 统计包括当前九宫格内元素的和
                sumthis = 0
                # 统计当前九宫格内非有效元素的个数，用于求均值
                numextra = 0
                # 求九宫格内有效元素的和
                for digit in total:
                    if digit != -10:
                        sumthis += digit
                    else:
                        numextra += 1
                # 求均值并赋给原矩阵对应元素
                M[i - 1][j - 1] = sumthis // (9 - numextra)
        return M


if __name__ == '__main__':
    solution = Solution()
    print(solution.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
