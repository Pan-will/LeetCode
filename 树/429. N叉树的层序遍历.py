"""
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :

返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        self.dfs(1, root, ans)
        return ans

    def dfs(self, level, root, ans):
        if len(ans) < level:
            ans.append([])
        ans[level].append(root.val)
        # 递归遍历子树
        for tNode in root.children:
            self.dfs(level + 1, tNode, ans)
        return ans
