"""
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

示例：
输入：[1,2,3,4,5,null,7,8]

        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 层序模板，百试不爽。
    def listOfDepth(self, tree):
        """
        :type tree: TreeNode
        :rtype: List[ListNode]
        """
        if not tree:
            return []
        ans = []
        stack = [tree]
        while stack:
            sizeStack = len(stack)
            # 初始化头结点
            head = ListNode(None)
            temp = head
            for i in range(sizeStack):
                node = stack.pop(0)
                temp.next = ListNode(node.val)
                temp = temp.next
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            # 结果中是不要头结点的
            ans.append(head.next)
        return ans
