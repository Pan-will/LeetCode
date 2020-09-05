"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = []
        if numRows == 0:
            return a
        # 初始化
        for i in range(1, numRows + 1):
            a.append([0] * i)
        print(a)
        # 最顶端元素
        a[0][0] = 1
        for i in range(1, numRows):
            for j in range(i + 1):
                # 每一行第一个和最后一个元素都是1
                if j == i or j == 0:
                    a[i][j] = 1
                # 否则是肩上两个元素之和
                else:
                    a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))