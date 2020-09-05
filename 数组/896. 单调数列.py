"""
判断数列是否单调。

示例 1：
输入：[1,2,2,3]
输出：true

示例 2：
输入：[6,5,4,4]
输出：true

示例 3：
输入：[1,3,2]
输出：false
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 1
        while i < len(A):
            if A[i] == A[i - 1]:
                i += 1
            # 递增
            elif A[i] > A[i - 1]:
                for j in range(i, len(A)):
                    if A[j] < A[j - 1]:
                        return False
                break
            # 递减
            elif A[i] < A[i - 1]:
                for j in range(i, len(A)):
                    if A[j] > A[j - 1]:
                        return False
                break
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMonotonic([-1, -1, -1, -9, 2]))
