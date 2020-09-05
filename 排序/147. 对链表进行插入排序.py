"""
插入排序：
    插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
    每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
    重复直到所有输入数据插入完为止。


从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

示例 1：
输入: 4->2->1->3
输出: 1->2->3->4

示例 2：
输入: -1->5->3->4->0
输出: -1->0->3->4->5

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # 原链表增加一个头结点，值为无穷小
        pre = ListNode(float('-Inf'))
        pre.next = head
        # 记录已排序的尾结点
        ok_end = pre
        # 遍历指针
        cur = head
        while cur:
            # 若当前结点值不小于已排序部分尾结点的值,则指针顺移
            if cur.val >= ok_end.val:
                ok_end = ok_end.next
                cur = cur.next
                continue
            # 断开当前结点
            ok_end.next = cur.next
            cur.next = None
            # 从头开始找插入位置
            temp = pre
            while temp.next and temp.next.val < cur.val:
                temp = temp.next
            # 插入当前结点
            cur.next = temp.next
            temp.next = cur
            # 遍历指针回位
            cur = ok_end.next

        return pre.next



if __name__ == '__main__':
    list = [4, 2, 1, 3]
    node = ListNode(0)
    head = ListNode(0)
    head.next = node
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    ans = Solution().insertionSortList(head.next.next)
    while ans:
        print(ans.val)
        ans = ans.next
