"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 3
输出: [1,3,3,1]
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a = []
        # 初始化
        for i in range(1, rowIndex + 2):
            a.append([0] * i)
        # 最顶端元素
        a[0][0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i + 1):
                # 每一行第一个和最后一个元素都是1
                if j == i or j == 0:
                    a[i][j] = 1
                # 否则是肩上两个元素之和
                else:
                    a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
        # 返回最后一个list
        return a[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(3))
