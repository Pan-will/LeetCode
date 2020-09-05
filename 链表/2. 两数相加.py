"""
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 方法一：用现有节点存放结果（用l1存的，l1短则把l2的多余节点拼到l1上）。
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 进位
        extra = 0
        # 记录l1和l2的前一个节点
        pre1 = ListNode(0)
        pre2 = ListNode(0)
        ans = ListNode(0)
        ans.next = l1
        while l1 and l2:
            sum = l1.val + l2.val + extra
            temp = sum % 10
            l1.val = temp
            # 计算进位
            extra = int(sum / 10)
            # 指针后移
            pre1 = l1
            l1 = l1.next
            pre2 = l2
            l2 = l2.next

        # 若l1遍历完，l2没完
        if not l1 and l2:
            # 先把l2剩余部分接到l1后，pre1再跟着l2走
            pre1.next = l2
            while l2:
                sum = l2.val + extra
                temp = sum % 10
                extra = int(sum / 10)
                l2.val = temp
                pre1 = l2
                l2 = l2.next
            # 最后一位有进位且l2已遍历完
            if not l2 and extra:
                node = ListNode(0)
                node.val = extra
                pre1.next = node

        # 若l2遍历完，l1没完
        if not l2 and l1:
            while l1:
                sum = l1.val + extra
                temp = sum % 10
                extra = int(sum / 10)
                l1.val = temp
                pre1 = l1
                l1 = l1.next
            if not l1 and extra:
                node = ListNode(0)
                node.val = extra
                pre1.next = node

        # 若l1和l2都遍历完，进位不为0
        if not l1 and not l2 and extra:
            node = ListNode(0)
            node.val = extra
            pre1.next = node

        return ans.next

    # 方法二：新建链表来存放结果。
    def addTwoNumbers2(self, l1, l2):
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
            # 求当前位的总和
            sum = l1.val + l2.val + extra
            # 计算当前位的值
            node.next.val = sum % 10
            # 计算进位
            extra = int(sum / 10)
            # 顺移
            node = node.next
            l1 = l1.next
            l2 = l2.next
        # 取未遍历完的
        res = l1 or l2
        while res:
            node.next = ListNode(0)
            sum = res.val + extra
            node.next.val = sum % 10
            extra = int(sum / 10)
            node = node.next
            res = res.next
        # 最后一步还有进位
        if extra:
            node.next = ListNode(0)
            node.next.val = extra
        return pre.next




