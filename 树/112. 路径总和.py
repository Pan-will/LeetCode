"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 法一
    def hasPathSum(self, root, sumt):
        """
        :type root: TreeNode
        :type sumt: int
        :rtype: bool
        """
        if not root and sum:
            return False
        stack = [(root, [root.val])]
        while stack:
            node, temp = stack.pop()
            if not node.left and not node.right and sum(temp) == sumt:
                return True
            if node.left:
                stack.append((node.left, temp + [node.left.val]))
            if node.right:
                stack.append((node.right, temp + [node.right.val]))
        return False

