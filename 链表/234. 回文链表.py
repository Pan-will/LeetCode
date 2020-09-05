"""
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->3->2->1
输出: true
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 思路：遍历原链表，采用头插法倒置前半部分，然后遍历前后两部分判断回文。
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre1, pre2 = head, head
        prehead = None
        pre = head
        while pre2 and pre2.next:
            pre = pre1
            pre1 = pre1.next
            pre2 = pre2.next.next
            # 头插法倒置前半部分
            pre.next = prehead
            prehead = pre
        # 奇数个节点，则pre1应在顺移一位
        if pre2 is not None:
            pre1 = pre1.next
        # 遍历比较是否回文
        while pre and pre1:
            if pre.val != pre1.val:
                return False
            pre = pre.next
            pre1 = pre1.next
        return True

    # 思路：先统计各节点的值域，再用list判断是否回文。
    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l1 = []
        num = 0
        # 统计节点个数
        while head:
            num += 1
            l1.append(head.val)
            head = head.next
        l2 = l1[::-1]
        n = num / 2 if num % 2 == 0 else num // 2 + 1
        for i in range(n):
            if l1[i] != l2[i]:
                return False
        return True