"""
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。
如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。
分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:
输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        # 小于x的节点，ans.next是返回值
        small = ans = ListNode(-1)
        # 不小于x的节点
        big = head_big = ListNode(-1)
        # 遍历指针
        cur = head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            cur = cur.next
        # 将两个链表段拼接，小于x的在前，不小于x的在后
        big.next = None
        small.next = head_big.next
        return ans.next


if __name__ == '__main__':
    list = [1, 4, 3, 2, 5, 2]
    node = ListNode(0)
    head = ListNode(0)
    head.next = node
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    ans = Solution().partition(head.next.next, 3)
    while ans:
        print(ans.val)
        ans = ans.next
