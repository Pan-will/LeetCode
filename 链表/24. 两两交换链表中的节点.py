"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 同一种思路，两种写法
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head
        cur = ans.next
        while cur.next and cur.next.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = cur.next.next
            cur.next.next = temp
            cur = cur.next.next
        return ans.next

    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head
        cur = ans.next
        while cur.next and cur.next.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = temp.next.next
            cur.next.next = temp
            cur = temp
        return ans.next
