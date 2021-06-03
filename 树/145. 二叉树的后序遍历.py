"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 迭代
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        post_stack = []
        cur = root
        while post_stack or cur:
            while cur:
                ans.append(cur.val)
                post_stack.append(cur)
                cur = cur.right
            temp = post_stack.pop()
            cur = temp.left
        return ans[::-1]

    # 递归
    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal2(root.left) + self.postorderTraversal2(root.right) + [root.val]
