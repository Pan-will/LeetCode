"""
给定一个二叉树，在树的最后一行找到最左边的值。
示例 1:
输入:
    2
   / \
  1   3
输出:
1

示例 2:
输入:
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
输出:
7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # BFS
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        res = []
        stack = [root]
        while stack:
            sizestack = len(stack)
            temp = []
            for i in range(sizestack):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(temp)
        return res[-1][0]

    # BFS的改进，先右后左，直接返回最后一个节点的值
    def findBottomLeftValue3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return node.val

    # DFS
    def findBottomLeftValue2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, curdepth):
            if not node:
                return
            if curdepth > self.maxdepth:
                self.res = node.val
                self.maxdepth = curdepth
            dfs(node.left, curdepth + 1)
            dfs(node.right, curdepth + 1)

        self.maxdepth, self.res = 0, root.val
        dfs(root, 0)
        return self.res
