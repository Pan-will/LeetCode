"""
给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。

请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        if not list1:
            return None
        prea, cur = list1, list1
        for _ in range(a):
            prea = cur
            cur = cur.next
        preb = cur
        for _ in range(a, b+1):
            preb = cur
            cur = cur.next
        prea.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = cur
        preb.next = None
        return list1