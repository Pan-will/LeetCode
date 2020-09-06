"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
提示：节点总数 <= 1000
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 思路：
    #   层序遍历，套用模板，百试不爽。
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        stack = [root]
        # 外层while遍历树的层数
        while stack:
            temp = []
            sizeStack = len(stack)
            # 内层for遍历每一层（当前层）的所有节点
            for i in range(sizeStack):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(temp)
        return ans





