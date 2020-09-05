"""
实现一个函数，检查二叉树是否平衡。
在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。

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
    def isBalanced(self, root):
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
        resultLeft = self.isBalanced(root.left)
        resultRight = self.isBalanced(root.right)

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
