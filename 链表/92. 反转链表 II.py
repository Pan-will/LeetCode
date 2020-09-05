"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 边界处理
        if not head or not head.next or m == n:
            return head
        prehead, cur = None, head
        while m > 1:
            prehead = cur
            cur = cur.next
            m -= 1
            n -= 1
        # one和two分别是遍历指针和前部分不用反转的最后一个节点
        one, two = cur, prehead
        while n:
            temp = cur.next
            cur.next = prehead
            prehead = cur
            cur = temp
            n -= 1
        if two:
            two.next = prehead
        else:
            head = prehead
        one.next = cur
        return head

    def reverseBetween2(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 边界处理
        if not head or not head.next or m == n:
            return head
        # 返回值
        ans = ListNode(0)
        ans.next = head
        # 记录第m-1个节点
        pre = ListNode(0)
        for i in range(1, m):
            pre = head
            head = head.next
        # 反转部分的首节点
        prehead = ListNode(0)
        # 记录第n个节点
        pretail = head
        # 开始反转从m到n个节点
        for j in range(m, n + 1):
            temp = head.next
            head.next = prehead
            prehead = head
            head = temp
        # 若不是从首节点开始反转，则拼接前部分未反转的节点
        if m != 1:
            pre.next = prehead
        else:
            ans.next = prehead
        # 若n小于原链表长度，则拼接后部分未反转的节点
        if head:
            pretail.next = head
        return ans.next
