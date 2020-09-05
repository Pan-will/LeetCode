"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (not root.left and not root.right):
            return 0
        ans = []
        # 根节点算左叶子
        self.dfs(root, 1, ans)
        return sum(ans)

    def dfs(self, node, is_left, ans):
        if node:
            if not node.left and not node.right:
                if is_left:
                    ans.append(node.val)
            if node.left:
                self.dfs(node.left, 1, ans)
            if node.right:
                self.dfs(node.right, 0, ans)
        return ans
