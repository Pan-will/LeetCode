class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def fun(self, head, k):
        if not head: return None
        pre = head  # 记录头结点
        low, fast = head, head
        temp = low  # 记录low指针的前一个节点，后面用来断开连接
        while k > 0 and fast.next and fast.next.next:
            temp = low
            low = low.next
            fast = fast.next.next
            k -= 1
        temp.next = None
        fast.next = pre
        return low


if __name__ == '__main__':
    head = ListNode(None)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    s = Solution()
    phead = s.fun(head.next, 5)
    while phead:
        print(phead.val)
        phead = phead.next
