"""
给你一棵二叉树的根节点 root ，树中有 n 个节点，每个节点都有一个不同于其他节点且处于 1 到 n 之间的值。

另给你一个由 n 个值组成的行程序列 voyage ，表示 预期 的二叉树 先序遍历 结果。

通过交换节点的左右子树，可以 翻转 该二叉树中的任意节点。例，翻转节点 1 的效果如下：

请翻转 最少 的树中节点，使二叉树的 先序遍历 与预期的遍历行程 voyage 相匹配 。 

如果可以，则返回 翻转的 所有节点的值的列表。你可以按任何顺序返回答案。如果不能，则返回列表 [-1]。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 思路：每个节点的值都不同；所以一边遍历作对比，一边翻转节点；
class Solution(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []
        self.i = 0

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if self.dfs(root, voyage):
            return self.res
        return [-1]

    def dfs(self, root, path):
        if not root:
            return True
        if root.val != path[self.i]:
            return False
        self.i += 1
        if root.left and root.left.val != path[self.i]:
            self.res.append(root.val)
            return self.dfs(root.right, path) and self.dfs(root.left, path)
        return self.dfs(root.left, path) and self.dfs(root.right, path)
