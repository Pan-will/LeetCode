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
    def ReverseList2(self, pHead, m, n):
        if not pHead or not pHead.next or m == n:
            return pHead
        pre, ans = ListNode(0), ListNode(0)
        # 记录头指针
        ans.next = pHead
        # 前部分不用反转的直接过
        for i in range(m):
            pre = pHead
            pHead = pHead.next
        # 记录反转部分的首节点
        unhead = ListNode(0)
        # 记录第n个节点
        untail = pHead
        # 开始反转
        for j in range(m, n + 1):
            temp = pHead.next
            pHead.next = unhead
            unhead = pHead
            pHead = temp
        # 不是从头反转
        if m != 1:
            pre.next = unhead
        # 从头反转
        else:
            ans.next = unhead
        if pHead:
            untail.next = pHead
        return ans
