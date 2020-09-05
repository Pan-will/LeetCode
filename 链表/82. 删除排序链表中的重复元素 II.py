"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 转list去重，再新建链表返回结果。
    # 注，本题结果要保留节点的原顺序
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 转list
        tar = []
        while head:
            tar.append(head.val)
            head = head.next
        # 删除list中的重复元素且保留原序
        ans = []
        num = 0
        for i in range(len(tar)):
            if tar.count(tar[i]) == 1:
                ans.append(tar[i])
                num += 1
        # 转链表返回
        pre = node = ListNode(-1)
        for j in range(num):
            node.next = ListNode(0)
            node.next.val = ans[j]
            node = node.next
        return pre.next

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode('a')
        ans.next = head
        pre, cur = None, ans
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.val == cur.next.val:
                temp = cur.val
                while cur and cur.val == temp:
                    cur = cur.next
            pre.next = cur
        return head

    # 用字典统计
    # 用例 [-3,-1,-1,0,0,0,0,0,2] 返回值是：[2,-3]，预期结果是：[-3,2]，没能保持原序，蓝瘦。
    def deleteDuplicates3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = head.next
        while prev:
            print("test:", prev.val)
            prev = prev.next
        dictval = {}
        while head:
            if head.val not in dictval:
                dictval[head.val] = 1
            else:
                dictval[head.val] += 1
            head = head.next

        # 转链表返回
        pre = node = ListNode(0)
        for key, value in dictval.items():
            if value == 1:
                node.next = ListNode(0)
                node.next.val = key
                node = node.next
        return pre.next


if __name__ == '__main__':
    # list = [-3, -1, -1, 0, 0, 0, 0, 0, 2]
    list = [1, 1, 1, 2, 3]
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
    ans = Solution().deleteDuplicates3(head.next)
    while ans:
        print(ans.val)
        ans = ans.next
