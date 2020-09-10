"""
给定一个 N 叉树，找到其最大深度。
最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    # BFS
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        res = 0
        stack = [root]
        while stack:
            sizeStack = len(stack)
            for i in range(sizeStack):
                node = stack.pop(0)
                for item in node.children:
                    if item:
                        stack.append(item)
            res += 1
        return res

    # DFS
    def maxDepth2(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        return max(1 + self.maxDepth2(child) for child in root.children)
