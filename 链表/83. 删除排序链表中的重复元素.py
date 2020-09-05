"""
给定一个排好序的链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 法一：改变指针域
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 若空链表或者只有一个节点，则返回原链表
        if not (head and head.next):
            return head
        # 创建新节点
        prehead = ListNode(0)
        # 确定新节点的指针
        prehead.next = head
        # low从第一个节点开始遍历
        low = prehead.next
        # high从low的下一个节点开始遍历
        high = low.next
        while high:
            if high.val == low.val:
                low.next = high.next
            else:
                low = high
            # 不论值域等不等，high都要顺移一位
            high = high.next
        return prehead.next

    # 法二：改变值域
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 空链表或只有一个节点
        if not (head and head.next):
            return head
        low, high = head, head
        while high:
            if high.val != low.val:
                low = low.next
                low.val = high.val
            high = high.next
        low.next = None
        return head

