"""
输入：1,2,2,3,4,4,4,5
输出：1,3,5
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        ans = ListNode(0)
        ans.next = head
        pre, cur = None, ans
        while cur.next:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.val == cur.next.val:
                temp = cur.val
                while cur.val == temp:
                    cur = cur.next
                pre.next = cur
        return ans.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = None
    s = Solution()
    res = s.deleteDuplicates(node1)
    while res:
        print(res.val)
        res = res.next
