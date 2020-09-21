"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

 

例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        sum = 0
        def helper(root,sum):
            if root:
                # BST的中序序列是升序序列
                helper(root.right)
                sum += root.val
                root.val = sum
                helper(root.left)
        helper(root, sum)
        return root


    def convertBST2(self, root):
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
