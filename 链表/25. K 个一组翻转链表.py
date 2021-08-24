"""
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partRev(self, head, tail):
        if not head: return None
        res = None
        cur = head
        while cur != tail:
            temp = cur.next
            cur.next = res
            res = cur
            cur = temp
        return res

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        hair = head
        tail = head
        for i in range(k):
            if not tail:
                return head
            tail = tail.next
        newHead = self.partRev(hair, tail)
        hair.next = self.reverseKGroup(tail, k)
        return newHead


if __name__ == '__main__':
    s = Solution()
    list = [1, 2, 3, 4, 5]
    head = ListNode(0)
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    ans = Solution().oddEvenList2(head.next)
    while ans:
        print(ans.val)
        ans = ans.next
