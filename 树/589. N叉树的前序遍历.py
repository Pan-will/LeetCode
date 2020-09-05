"""
给定一个 N 叉树，返回其节点值的前序遍历。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    # 递归
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        return self.dfs(root, ans)

    def dfs(self, root, ans):
        ans.append(root.val)
        for node in root.children:
            self.dfs(node, ans)
        return ans

    # 迭代
    def preorder2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack += curr.children[::-1]
        return res
