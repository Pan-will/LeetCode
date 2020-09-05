"""
给出一个整数数组 A 和一个查询数组 queries。
对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index] 上。
然后，第 i 次查询的答案是 A 中偶数值的和。
（此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）
返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。

示例：
输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
输出：[8,6,2,4]
解释：
开始时，数组为 [1,2,3,4]。
将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
"""


class Solution(object):
    # 暴力超时
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(A)):
            A[queries[i][1]] += queries[i][0]
            temp = 0
            for j in range(len(A)):
                if A[j] % 2 == 0:
                    temp += A[j]
            ans.append(temp)
        return ans

    def sumEvenAfterQueries2(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # 返回值
        ans = []
        # 统计原list中偶数元素的和
        temp = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                temp += A[i]
        for j in range(len(A)):
            val = queries[j][0]
            index = queries[j][1]
            # 若将要改变的元素是偶数，则要从和中减掉
            if A[index] % 2 == 0:
                temp -= A[index]
            # 改变元素
            A[index] += val
            # 若改变以后是偶数，则要加到和中
            if A[index] % 2 == 0:
                temp += A[index]
            ans.append(temp)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumEvenAfterQueries(A=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]))
