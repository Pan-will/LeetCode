"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 题意要转成平衡二叉搜索树
    # 先转成list，在转BST呗。
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.digui(nums)

    def digui(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.digui(nums[:mid])
        root.right = self.digui(nums[mid + 1:])
        return root
