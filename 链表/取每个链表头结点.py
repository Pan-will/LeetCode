class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param a ListNode类一维数组 指向这些数链的开头
# @return ListNode类
class Solution:
    def solve(self, a):
        n = len(a)  # 首先取到链表数量
        res = ListNode(0)
        head = res
        for i in range(n):
            if a[i]:
                head.next = a[i]
                head = head.next
                a[i] = a[i].next
        return res.next


