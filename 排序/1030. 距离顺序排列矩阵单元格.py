"""
给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离按升序排，
其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。
（你可以按任何满足此条件的顺序返回答案。）

示例 1：
输入：R = 1, C = 2, r0 = 0, c0 = 0
输出：[[0,0],[0,1]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1]

思路：
声明矩阵list；
返回按曼哈顿距离排序的list；
"""


class Solution(object):

    def allCellsDistOrder2(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        dist = [[i, j] for i in range(R) for j in range(C)]
        dist.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return dist

    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        # 返回值
        dist_list = [[] for i in range(200)]
        # print(dist_list)
        # 计算距离并排序
        for i in range(R):
            for j in range(C):
                distinct = abs(r0 - i) + abs(c0 - j)
                # 将坐标插入距离对应的dist_list下标处
                dist_list[distinct].append([i, j])
        result = []
        # 遍历dist_list，不为空则添加到result中
        for i in dist_list:
            if i:
                result.extend(i)
            else:
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.allCellsDistOrder(R=1, C=2, r0=0, c0=0))
