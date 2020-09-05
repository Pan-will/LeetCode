"""
给定一个链表，判断链表中是否有环。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 思路：快慢指针。
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    # 思路：用list或set。
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        while head:
            if head in list:
                return True
            list.append(head)
            head = head.next
        return False
