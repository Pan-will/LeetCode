"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:
输入：[1, 2, 3, 3, 2, 1]
输出：[1, 2, 3]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        my_list = []
        temp = ListNode(-1)
        node = head
        while node:
            if node.val not in my_list:
                my_list.append(node.val)
                temp = node
                node = node.next
            else:
                temp.next = node.next
                node.next = None
                node = temp.next
        return head


if __name__ == '__main__':
    list = [1, 2, 3, 3, 2, 1]
    node = ListNode(0)
    head = ListNode(0)
    head.next = node
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    ans = Solution().removeDuplicateNodes(head.next.next)
    while ans:
        print(ans.val)
        ans = ans.next
