"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
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


if __name__ == '__main__':
    s = Solution()
    r = TreeNode(1)
    l1 = TreeNode(2)
    l2 = TreeNode(2)
    l4 = TreeNode(3)
    l5 = TreeNode(4)
    l6 = l5
    l7 = l4
    r.left = l1
    r.right = l2
    l1.left = l4
    l1.right = l5
    l2.left = l6
    l2.right = l7
    print(s.isSymmetric(r))
