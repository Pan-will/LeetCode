"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 迭代
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        pre_stack = [root]
        ans = []
        while pre_stack:
            cur = pre_stack.pop()
            ans.append(cur.val)
            if cur.right:
                pre_stack.append(cur.right)
            if cur.left:
                pre_stack.append(cur.left)
        return ans

    # 迭代
    def preorderTraversal3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        pre_stack = []
        ans = []
        cur = root
        while pre_stack or cur:
            while cur:
                ans.append(cur.val)
                pre_stack.append(cur)
                cur = cur.left
            temp = pre_stack.pop()
            cur = temp.right
        return ans

    # 递归
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return [root.val] + self.preorderTraversal2(root.left) + self.preorderTraversal2(root.right)
