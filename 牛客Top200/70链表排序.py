class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 链表快速排序
class Solution:
    def sortInList(self, head):
        if not head or not head.next:
            return head
        ans = ListNode(-1)
        ans.next = head
        return self.quickSort(ans, None)

    # 快速排序
    def quickSort(self, head, end):
        if head == end or head.next == end or head.next.next == end:
            return head
        tpmHead = ListNode(-1)
        # 划分节点
        poi = head.next
        # 遍历指针
        cur = poi
        pre = tpmHead
        # 一趟划分
        while cur.next != end:
            # 当前节点值域小于划分节点的值域，则将当前节点放到左侧
            if cur.next.val < poi.val:
                pre.next = cur.next
                pre = pre.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        # 合并临时链表和原链表，将原链表接到临时链表后面即可
        pre.next = head.next
        head.next = tpmHead.next
        self.quickSort(head, poi)
        self.quickSort(poi, end)
        return head.next
