"""
给你一个大小为 m * n 的方阵 mat，方阵由若干军人和平民组成，分别用 1 和 0 表示。
请你返回方阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。
如果第i行的军人数量少于第j行，或者两行军人数量相同但i小于j，那么我们认为第i行的战斗力比第j行弱。
军人总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

示例 1：
输入：mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
输出：[2,0,3]
解释：
每行中的军人数目：
行 0 -> 2
行 1 -> 4
行 2 -> 1
行 3 -> 2
行 4 -> 5
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
"""


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        power = [sum(line) for line in mat]
        return sorted(list(range(len(mat))), key=lambda i: (power[i], i), reverse=False)[:k]


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.kWeakestRows(mat=[[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]],
                              k=3))
