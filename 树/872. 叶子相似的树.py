"""
请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        self.dfs(root1, res1)
        res2 = []
        self.dfs(root2, res2)
        return res1 == res2

    # DFS找二叉树的叶子节点
    def dfs(self, root, res):
        if not root:
            return []
        elif not root.left and not root.right:
            res.append(root.val)
        else:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
        return res
