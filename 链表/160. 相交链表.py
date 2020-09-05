"""
编写一个程序，找到两个单链表相交的起始节点。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 思路：指针a,b分别从headA和headB遍历，到尾后，b再从headA遍历，a从headB遍历；
    # 当a==b时记录下此节点ans，若此后到尾一直相等则返回ans。
    # 交叉遍历，可以保证不论两个链表哪个长，指针遍历的节点数一样多。
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while a:
            a = a.next
        a.next = headB
        while b:
            b = b.next
        b.next = headA
        while a != b:
            a = a.next
            b = b.next
        return a

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
