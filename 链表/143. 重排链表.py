"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.

示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        pre = head
        # 用快慢指针找链表中间节点,循环结束时：slow.next指向中间节点。
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 原链表的后半段
        rev = slow.next
        # 反转原链表的后半段
        behind = None
        while rev:
            temp = rev.next
            rev.next = behind
            behind = rev
            rev = temp
        # 断开原链表的前半段
        slow.next = None
        # pre = pre.next
        while pre and behind:
            temp1 = pre.next
            temp2 = behind.next
            pre.next = behind
            behind.next = temp1
            behind = temp2
            pre = temp1
        # return head

    def reorderList2(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        next = []
        pre, cur = head, head
        while pre:
            next.append(pre)
            pre = pre.next
        num = len(next)
        while num > 0:
            cur.next = next[0]
            next.pop(0)
            next = next[::-1]
            cur = cur.next
            num -= 1
        cur.next = None


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]
    node = ListNode(0)
    head = ListNode(0)
    head.next = node
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    Solution().reorderList(head.next)
    while head:
        print(head.val)
        head = head.next
