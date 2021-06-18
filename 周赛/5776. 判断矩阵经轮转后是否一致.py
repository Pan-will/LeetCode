import numpy as np


class Solution(object):
    def judge(self, mat, tar):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != tar[i][j]:
                    return False
        return True

    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        mat = np.array(mat)
        target = np.array(target)
        for i in range(1, 5):
            temp = np.rot90(mat, i)
            if self.judge(temp, target):
                return True
            else:
                continue
        return False


if __name__ == '__main__':
    s = Solution()

    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]

    print(s.findRotation(mat, target))
