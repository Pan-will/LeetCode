"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 特判：根节点为空
        if not root:
            return 0
        # 特判：只有根节点
        if not root.left and not root.right:
            return 1
        res = 1
        # BFS
        stack = [root]
        while stack:
            lenstack = len(stack)
            for i in range(lenstack):
                node = stack.pop(0)
                if not node.left and not node.right:
                    return res
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res += 1
        return res
