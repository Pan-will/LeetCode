"""
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请使用原地算法完成。空间复杂度应为 O(1)，时间复杂度应为 O(n)。

示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        ji = head_ji = ListNode(-1)
        ou = head_ou = ListNode(-1)
        cur = head
        flag = 1
        while cur:
            # 奇数位节点
            if flag:
                ji.next = cur
                ji = ji.next
                flag = 0
            # 偶数位节点
            else:
                ou.next = cur
                ou = ou.next
                flag = 1
            cur = cur.next
        ou.next = None
        ji.next = head_ou.next
        return head_ji.next

    def oddEvenList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next or not head.next.next:
            return head
        ji, ou = ListNode(-1), ListNode(-1)
        cur = head
        pre_ji, pre_ou = ji, ou
        flag = 1
        while cur:
            temp = cur.next
            if flag % 2 == 1:
                ji.next = cur
                ji = ji.next
                flag = 0
            else:
                ou.next = cur
                ou = ou.next
            cur = temp
        ou.next = None
        ji.next = pre_ou.next
        return pre_ji.next

    def oddEvenList3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next or not head.next.next:
            return head
        ji = head.next
        pre = ou = head.next.next
        while ou:
            ji.next = ji.next.next
            ou.next = ou.next.next
            ji = ji.next
            ou = ou.next
        ji.next = pre
        return head


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]
    node = ListNode(0)
    head = ListNode(0)
    head.next = node
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    ans = Solution().oddEvenList2(head.next)
    while ans:
        print(ans.val)
        ans = ans.next
