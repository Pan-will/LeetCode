# encoding="utf-8"
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 法一：自底向上
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root) >= 0

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    # 法二：自顶向下
    def isBalanced2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        # 左、右子树深度
        heightLeft = self.treeDepth(root.left)
        heightRight = self.treeDepth(root.right)
        # 判断左、右子树是否平衡
        resultLeft = self.isBalanced2(root.left)
        resultRight = self.isBalanced2(root.right)

        # 左子树和右子树都是AVL，并且高度相差不大于1，返回真
        if resultLeft and resultRight and abs(heightLeft - heightRight) <= 1:
            return True
        else:
            return False

    # 求二叉树的深度
    def treeDepth(self, root):
        if not root:
            return 0
        depthLeft = self.treeDepth(root.left)
        depthRight = self.treeDepth(root.right)
        return depthLeft + 1 if depthLeft > depthRight else depthRight + 1
