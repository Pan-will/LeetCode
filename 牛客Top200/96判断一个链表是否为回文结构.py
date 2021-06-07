class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 头尾指针，判断值域是否相等
    def isPail(self, head):
        if not head or not head.next:
            return True
        # 寻找链表中点
        pre = head
        slow, fast = head, head
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        # 链表从中间断开
        pre.next = None
        # 反转后半段
        head2 = None
        while slow:
            temp = slow.next
            slow.next = head2
            head2 = slow
            slow = temp
        # 判断回文
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

