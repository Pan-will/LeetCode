"""
给定一个矩阵 A， 返回 A 的转置矩阵。
矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
"""


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        hang = len(A)
        lie = len(A[0])
        ans = []
        for i in range(lie):
            temp = []
            for j in range(hang):
                temp.append(A[j][i])
            ans.append(temp)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
