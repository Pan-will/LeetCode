"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 递归思路：
    # （1）如果二叉树为空，二叉树的深度为0
    # （2）如果二叉树不为空，二叉树的深度 = max(左子树深度， 右子树深度) + 1
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depthLeft = self.maxDepth(root.left)
        depthRight = self.maxDepth(root.right)
        return depthLeft + 1 if depthLeft > depthRight else depthRight + 1
