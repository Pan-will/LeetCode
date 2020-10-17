"""
给定一个二叉树，返回它的中序遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""


# Definition for a binary tree node.
# 二叉树的结点结构
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 迭代
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        mid_stack = []
        ans = []
        cur = root
        while cur or mid_stack:
            while cur:
                mid_stack.append(cur)
                cur = cur.left
            temp = mid_stack.pop()
            ans.append(temp.val)
            cur = temp.right
        return ans

    # 递归
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal2(root.left) + [root.val] + self.inorderTraversal2(root.right)