"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
"""


class Solution(object):
    # 二分查找
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        while low < high:
            # 计算矩阵中值
            mid = low + int((high - low) / 2)
            # 统计小于等于mid的元素个数
            count = 0
            i, j = 0, n - 1
            while j >= 0 and i < n:
                if matrix[i][j] <= mid:
                    count += j + 1
                    i += 1
                else:
                    j -= 1

            if count < k:
                low = mid + 1
            else:
                high = mid
        return low

    # 暴力
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        temp = []
        for i in range(len(matrix)):
            temp += matrix[i]
        temp.sort()
        return temp[k - 1]

    # 暴力
    def kthSmallest3(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        temp = matrix[0]
        for i in range(1, m):
            for j in range(n):
                temp.append(matrix[i][j])
        temp.sort()
        return temp[k - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kthSmallest(matrix=[
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]], k=8))
