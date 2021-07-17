"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # 求左子树深度
        leftDenth = self.treeDepth(root.left)
        rightDenth = self.treeDepth(root.right)
        resLeft = self.isBalanced(root.left)
        resRight = self.isBalanced(root.right)
        if resLeft and resRight and abs(leftDenth-rightDenth)<=1:
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
