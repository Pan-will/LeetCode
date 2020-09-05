"""
给定一个 N 叉树，返回其节点值的后序遍历。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    # 迭代
    def postorder(self, root):
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
            stack += curr.children
        return res[::-1]

    # 递归
    def postorder2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        # 递归遍历子树
        for tNode in root.children:
            res += self.postorder2(tNode)
        # 加根节点
        res.append(root.val)
        return res