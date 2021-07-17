"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 方法一：BFS
    # 思路：层序模板。
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans = []
        stack = [root]
        while stack:
            l = len(stack)
            temp = []
            for i in range(l):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(temp)
        return len(ans)

    # 方法一：DFS
    # 思路：树的深度 = 根的左子树深度+1 或 右子树深度+1
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftDepth = self.maxDepth2(root.left)
        rightDepth = self.maxDepth2(root.right)
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1
