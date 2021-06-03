class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow, fast = head, head
        meet = ListNode(0)
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = fast
                break
        while head and meet:
            if head == meet:
                return head
            head = head.next
            meet = meet.next
        return None
