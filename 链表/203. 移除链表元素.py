"""
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# 已定义的单链表：
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prehead = ListNode(-1)
        prehead.next = head
        pre = prehead
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return prehead.next

