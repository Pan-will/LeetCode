# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 从头到尾反转链表
    def ReverseList(self, pHead):
        pre, cur = None, pHead
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        pHead = pre
        return pHead

    # 反转链表中（m,n）个节点
    def ReverseList2(self, head, m, n):
        if not head or not head.next or m == n:
            return head
        pre, ans = None, ListNode(0)
        ans.next = head
        for i in range(1, m):
            pre = head
            head = head.next
        #       反转部分首节点
        prehead = None
        #       反转部分尾节点
        tail = head
        for j in range(m, n + 1):
            temp = head.next
            head.next = prehead
            prehead = head
            head = temp
        #       不是从头反转的
        if m != 1:
            pre.next = prehead
        else:
            ans.next = prehead
        #       n并非最后一个节点
        if head:
            tail.next = head
        return ans.next
