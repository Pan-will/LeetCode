"""
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    递归：
        终止条件是两个节点都为空,return True
        或者两个节点中有一个为空,return False
        或者两个节点的值不相等,return False
    """

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.digui(root.left, root.right)

    def digui(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if left and not right:
            return False
        if left.val != right.val:
            return False
        return self.digui(left.left, right.right) and self.digui(left.right, right.left)
