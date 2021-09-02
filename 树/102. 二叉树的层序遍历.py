# coding = utf-8
"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。
（即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

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
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 相当于广度优先搜索，使用队列实现。
    # 队列初始化，将根节点压入队列。
    # 当队列不为空，进行如下操作：
    # 弹出一个节点，访问，若左子节点或右子节点不为空，将其压入队列。
    def levelOrder(self, root):
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
        return ans

    # 递归
    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        self.bfs(1, root, ans)
        return ans

    def bfs(self, level, root, ans):
        if len(ans) < level:
            ans.append([])
        ans[level - 1].append(root.val)
        if root.left:
            self.bfs(level + 1, root.left, ans)
        if root.right:
            self.bfs(level + 1, root.right, ans)
        return ans

    def levelOrder3(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            temp = []
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
        return ans



