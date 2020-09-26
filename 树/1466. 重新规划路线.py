"""
n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。
因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。
去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。
路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。
今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。
请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。
题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。

示例 1：
输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
"""


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # 记录所有点的出、入度:0表示入度，1表示出度
        edge = [[] for _ in range(n)]
        # 遍历参数中的边，每条边的两个端点都要记录相应的出、入度
        for start, end in connections:
            edge[start].append((end, 1))
            edge[end].append((start, 0))
        print(edge)
        # 设置每个点的访问标记，避免重复访问；对于本题，0点初始化是已访问的
        visit = [False] * n
        visit[0] = True
        # 返回值
        ans = 0
        # 开始BFS
        already = [0]
        while already:
            cur = already.pop(0)
            print(visit, edge[cur])
            for index, degree in edge[cur]:
                if not visit[index]:
                    visit[index] = True
                    ans += degree
                    already.append(index)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minReorder(5, [[4, 3], [2, 3], [1, 2], [1, 0]]))
