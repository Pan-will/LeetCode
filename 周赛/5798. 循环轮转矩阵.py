"""
输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
"""


class Solution(object):
    def nishizhen(self, nums, k):
        nums[:] = (nums[i] for i in range(-(len(nums) - k % len(nums)), k % len(nums)))
        return nums

    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if not grid:
            return res
        beginRow = 0
        endRow = len(grid) - 1
        beginCol = 0
        endCol = len(grid[0]) - 1
        while beginRow <= endRow and beginCol <= endCol:
            cur = []
            for i in range(beginCol, endCol + 1):
                cur.append(grid[beginRow][i])
            beginRow += 1
            for i in range(beginRow, endRow + 1):
                cur.append(grid[i][endCol])
            endCol -= 1
            if beginRow <= endRow:
                # range函数是左开右闭的
                for i in range(endCol, beginCol - 1, -1):
                    cur.append(grid[endRow][i])
                endRow -= 1
            if beginCol <= endCol:
                for i in range(endRow, beginRow - 1, -1):
                    cur.append(grid[i][beginCol])
                beginCol += 1
            res.append(cur)
        for i, nums in enumerate(res):
            res[i] = self.nishizhen(nums, k)

        return self.reseve(res, len(grid), len(grid[0]))

    def reseve(self, origin, m, n):
        res = []
        for i in range(m):
            res.append([0] * n)

        beginRow = 0
        endRow = len(res) - 1
        beginCol = 0
        endCol = len(res[0]) - 1
        level = 0
        while beginRow <= endRow and beginCol <= endCol and level < len(origin):
            temp = origin[level]
            for i in range(beginCol, endCol + 1):
                res[beginRow][i] = temp.pop(0)
            beginRow += 1
            for i in range(beginRow, endRow + 1):
                res[i][endCol] = temp.pop(0)
            endCol -= 1
            if beginRow <= endRow:
                for i in range(endCol, beginCol - 1, -1):
                    res[endRow][i] = temp.pop(0)
                endRow -= 1
            if beginCol <= endCol:
                for i in range(endRow, beginRow - 1, -1):
                    res[i][beginCol] = temp.pop(0)
                beginCol += 1
            level += 1
        return res


if __name__ == '__main__':
    s = Solution()
    # grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # print(s.rotateGrid(grid, k=2))
    print(s.rotateGrid([[40, 10], [30, 20]], 1))
