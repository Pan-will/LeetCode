class Solution:
    # 将矩阵顺时针旋转n次
    def rotateMatrix_n(self, mat, k):
        if not mat: return None
        for _ in range(k):
            mat = self.rotateMatrix(mat)
        return mat

    # 将矩阵顺时针旋转1次
    def rotateMatrix(self, mat):
        ans = []
        n = len(mat)
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(mat[n - j - 1][i])
            ans.append(temp)
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.rotateMatrix(
    #     [[1, 2],
    #      [4, 5]], 2))
    print(s.rotateMatrix_n(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]], 3))
