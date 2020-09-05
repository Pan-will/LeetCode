"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 先特判：
    #   当节点root为空时：return None;
    #   当p或q的值域等于root时，return root;
    # 再递归判断root的左、右子树；
    #   若左右子树都不为空：return root;
    #   若左真右假：return 左;
    #   若左假右真：return 右;
    #   否则，左右都为空：return None;
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        elif left and not right:
            return left
        elif not left and right:
            return right
        else:
            return None

