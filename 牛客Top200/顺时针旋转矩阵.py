class Solution:
    def rotateMatrix(self, mat, n):
        ans = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(mat[n - j - 1][i])
            ans.append(temp)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.rotateMatrix(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))
