"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # list
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mylist = []
        while head:
            if head in mylist:
                return head
            else:
                mylist.append(head)
            head = head.next
        return None

    # 快慢指针
    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                fast = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
