"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 思路：
# 1、遍历原链表，分别找到小于x的节点与大于等于x的节点组成的两个链表small和big;
# 2、拼接small和big，small在前。

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        # 小于x的节点，ans.next是返回值
        small = ans = ListNode(-1)
        # 不小于x的节点
        big = head_big = ListNode(-1)
        # 遍历指针
        cur = head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            cur = cur.next
        # 将两个链表段拼接，小于x的在前，不小于x的在后
        big.next = None
        small.next = head_big.next
        return ans.next
