"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        node = head
        len = 0
        while node:
            len += 1
            node = node.next
        if len < 2 or len == k:
            return head
        k %= len
        cur, tail = head, head
        precur = ListNode(0)
        while k > 1 and tail.next:
            tail = tail.next
            k -= 1
        while tail.next:
            precur = cur
            cur = cur.next
            tail = tail.next
        tail.next = head.next
        precur.next = None
        head = cur
        return head

    def rotateRight2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tail = head
        res = []
        while tail:
            res.append(tail.val)
            tail = tail.next
        if len(res) == 0:
            return head
        k = k % len(res)
        while k > 0:
            temp = res.pop()
            res.insert(0, temp)
            k -= 1
        pre = node = ListNode(0)
        for i in range(len(res)):
            node.next = ListNode(0)
            node.next.val = res[i]
            node = node.next
        return pre.next


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]
    distance = 10

    node = ListNode(0)
    head = ListNode(0)
    head.next = node
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    # while head.next:
    #     print(head.next.val)
    #     head = head.next
    ans = Solution().rotateRight(head.next, distance)
    while ans:
        print(ans.val)
        ans = ans.next
