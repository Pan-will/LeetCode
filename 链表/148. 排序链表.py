"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """***********************链表归并排序**********************"""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sortList0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 用快慢指针找链表中间节点,循环结束时：slow.next指向中间节点。
        slow, fast = head, head
        pre = None
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if not pre:
            return head
        pre.next = None
        # 对左右两个部分分别使用归并排序
        left = self.sortList0(head)
        right = self.sortList0(slow)

        cur = ans = ListNode(-1)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left if left else right
        return ans.next

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """***********************链表归并排序**********************"""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sortList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 用快慢指针找链表中间节点,循环结束时：slow.next指向中间节点。
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 对右半部分归并排序
        right = self.sortList1(slow.next)
        # 断开左右两部分链表
        slow.next = None
        # 对左半部分归并排序
        left = self.sortList1(head)
        return self.mergeLink(left, right)

    # 合并两个链表：按升序
    def mergeLink(self, left, right):
        node = ListNode(-1)
        head = node
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        node.next = left if left else right
        return head.next

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """***********************链表快排**************************"""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sortList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        ans = ListNode(-1)
        ans.next = head
        return self.quickSort(ans, None)

    # 快速排序
    def quickSort(self, head, end):
        if head == end or head.next == end or head.next.next == end:
            return head
        tpmHead = ListNode(-1)
        # 划分节点
        poi = head.next
        # 遍历指针
        cur = poi
        pre = tpmHead
        # 一趟划分
        while cur.next != end:
            # 当前节点值域小于划分节点的值域，则将当前节点放到左侧
            if cur.next.val < poi.val:
                pre.next = cur.next
                pre = pre.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        # 合并临时链表和原链表，将原链表接到临时链表后面即可
        pre.next = head.next
        head.next = tpmHead.next
        self.quickSort(head, poi)
        self.quickSort(poi, end)
        return head.next

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """***********************链表快排**************************"""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sortList3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev
            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]

        def quicksort(start, end):
            if start.next != end:
                prev, post = partition(start, end)
                quicksort(start, prev)
                quicksort(post, end)

        ans = ListNode(0)
        ans.next = head
        quicksort(ans, None)
        return ans.next


if __name__ == '__main__':
    list = [4, 2, 5, 3, 7, 9, 6, 1]
    node = ListNode(0)
    head = ListNode(0)
    head.next = node
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    ans = Solution().sortList1(head.next)
    ans = ans.next
    while ans:
        print(ans.val)
        ans = ans.next
