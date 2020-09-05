"""
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。

示例：
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
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
        pre = node = ListNode(0)
        # 进位
        extra = 0
        while l1 and l2:
            node.next = ListNode(0)
            sum = l1.val + l2.val + extra
            node.next.val = sum % 10
            extra = int(sum / 10)
            node = node.next
            # 指针顺移
            l1 = l1.next
            l2 = l2.next
        res = l1 or l2
        while res:
            # 新建节点必须在while里面，满足循环条件才新建
            node.next = ListNode(0)
            sum = res.val + extra
            node.next.val = sum % 10
            extra = int(sum / 10)
            node = node.next
            # 指针顺移
            res = res.next
        if extra:
            node.next = ListNode(0)
            node.next.val = extra
        return pre.next
