"""
给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。
已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getDecimalValue(self):
        """
        :type head: ListNode
        :rtype: int
        """
        list = []
        while head:
            list.append(head.val)
            head = head.next
        list = list[::-1]
        ans = 0
        for i in range(len(list)):
            ans += list[i] * (2 ** i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.getDecimalValue())
