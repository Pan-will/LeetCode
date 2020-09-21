"""
同538题。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        # BST的中序序列是升序序列
        res = self.midOrder(root)

        return self.helper(root, res)

    # 返回中序序列
    def midOrder(self, root):
        if not root:
            return []
        res = []
        res += self.midOrder(root.left)
        res.append(root.val)
        res += self.midOrder(root.right)
        return res

    def helper(self, root, res):
        if not root:
            return
        cur = res.index(root.val)
        root.val = sum(res[cur:])
        root.left = self.helper(root.left, res)
        root.right = self.helper(root.right, res)
        return root