# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return void
#
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        pre = slow.next
        slow.next = None
        # 反转后半部分
        head2 = None
        while pre:
            temp = pre.next
            pre.next = head2
            head2 = pre
            pre = temp
        p1 = head
        p2 = head2
        while p1 and p2:
            p1_tmp = p1.next
            p2_tmp = p2.next
            p1.next = p2
            p1 = p1_tmp
            p2.next = p1
            p2 = p2_tmp
