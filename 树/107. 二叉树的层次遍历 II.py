"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level_queue = []
        ans = []
        level_queue.append(root)
        while level_queue:
            num = len(level_queue)
            temp = []
            while num > 0:
                cur = level_queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    level_queue.append(cur.left)
                if cur.right:
                    level_queue.append(cur.right)
                num -= 1
            ans.append(temp)
        return ans[::-1]

    def levelOrderBottom2(self, root):
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            temp = []
            l = len(queue)
            for i in range(l):
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(temp)
        return ans[::-1]