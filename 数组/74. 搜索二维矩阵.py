class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        temp = []
        for i in range(len(matrix)):
            if matrix[i][0] == target or matrix[i][-1] == target:
                return True
            elif matrix[i][0] < target < matrix[i][-1]:
                temp = matrix[i]
                break
            else:
                continue
        l, r = 0, len(temp) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if temp[mid] == target:
                return True
            elif temp[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1]], 1))
    # print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
    print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
