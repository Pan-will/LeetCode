"""
给一个有 n 个结点的有向无环图，找到所有从 0 到 n-1 的路径并输出（不要求按顺序）
二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点
（译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a ）空就是没有下一个结点了。
 

示例 1：
输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
"""


class Solution(object):
    # 方法一：DFS
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if not graph[0]:
            return []
        res = []
        n = len(graph)
        self.dfs(graph, 0, n - 1, [0], res)
        return res

    def dfs(self, graph, cur, end, temp, res):
        # 递归出口：当前节点是n-1时，说明找到一条新路径
        if temp[-1] == end:
            res.append(temp)
            return
        # 顺着当前节点往下走
        for i in graph[cur]:
            self.dfs(graph, i, end, temp + [i], res)

    # 方法二：BFS
    def allPathsSourceTarget2(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # 特判
        if not graph[0]:
            return []
        # 路径终点
        end = len(graph) - 1
        res = []
        # 队列初始化
        nodeQueue = [0]
        pathQueue = [[0]]
        while nodeQueue:
            node = nodeQueue.pop(0)
            path = pathQueue.pop(0)
            # 遍历当前节点能达到的所有节点
            for i in graph[node]:
                # 若当前节点是终点，则找到一条新路径
                if i == end:
                    res.append(path + [i])
                # 否则，当前节点先入队，并更新当前路径
                else:
                    nodeQueue.append(i)
                    pathQueue.append(path + [i])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget2(graph=[[1, 2], [3], [3], []]))
