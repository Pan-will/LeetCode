class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 用递归
    # 每次找到头尾节点
    def reverseKGroup(self, head, k):
        if not head:
            return None
        low, fast = head, head
        for _ in range(k):
            if not fast:
                return head
            fast = fast.next

        def reverse(low, fast):
            pre = ListNode(0)
            pre.next = low
            while low != fast:
                temp = low.next
                low.next = pre
                pre = low
                low = temp
            return pre

        phead = reverse(low, fast)
        low.next = self.reverseKGroup(fast, k)
        return phead

