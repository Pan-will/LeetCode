"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(A)):
            ans.append(A[i] * A[i])
        return sorted(ans)

    def sortedSquares2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x ** 2 for x in A])


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortedSquares2([-4, -1, 0, 3, 10]))
