"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。
它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例：
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # step1：先反转l1和l2
        link1 = None
        while l1:
            temp = l1.next
            l1.next = link1
            link1 = l1
            l1 = temp
        link2 = None
        while l2:
            temp = l2.next
            l2.next = link2
            link2 = l2
            l2 = temp

        # step2：两数相加
        pre = node = ListNode(0)
        # 进位
        extra = 0
        while link1 and link2:
            node.next = ListNode(0)
            # 求当前位的总和
            sum = link1.val + link2.val + extra
            # 计算当前位的值
            node.next.val = sum % 10
            # 计算进位
            extra = int(sum / 10)
            # 顺移
            node = node.next
            link1 = link1.next
            link2 = link2.next

        res = link1 or link2
        while res:
            node.next = ListNode(0)
            sum = res.val + extra
            node.next.val = sum % 10
            extra = int(sum / 10)
            node = node.next
            res = res.next
        if extra:
            node.next = ListNode(0)
            node.next.val = extra

        # step3：反转结果链表
        pre = pre.next
        ans = None
        while pre:
            temp = pre.next
            pre.next = ans
            ans = pre
            pre = temp
        return ans
