"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            sizestack = len(stack)
            for i in range(sizestack):
                node = stack.pop(0)
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res

    def layer(self, root):
        if not root:
            return []
        ans = []
        layer_stack = [root]
        while layer_stack:
            num = len(layer_stack)
            temp = []
            while num > 0:
                cur = layer_stack.pop(0)
                temp.append(cur.val)
                if cur.left:
                    layer_stack.append(cur.left)
                if cur.right:
                    layer_stack.append(cur.right)
                num -= 1
            ans.append(temp)
        return ans