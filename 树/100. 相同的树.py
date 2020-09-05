"""
给定两个二叉树，检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
输出: true
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 根节点值不同，树不同
        if p.val != q.val:
            return False
        # 左右子树有一个不同，树不同
        if not p or not q:
            return False
        # 根节点值相同且左右子树均为空，树相同
        if not p and not q:
            return True
        # 递归判断左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
