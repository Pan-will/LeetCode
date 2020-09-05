"""
将两个升序链表合并为一个新的升序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# 已定义的单链表：
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
思路：需要注意的就是指针的指向处理。
    pre指针跟随l1和l2中值较小者向后顺移，每一步指向二者中的较小者，负责确立指向关系；
    若l1>=l2,pre指向l2，l2向后顺移一位。否则pre指向l1，l1向后顺移。
"""
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 返回值链表的头指针
        prehead = ListNode(-1)
        pre = prehead
        while l1 and l2:
            if l1.val >= l2.val:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next
        # 把未遍历到的节点接到新链表的后面
        pre.next = l1 if l1 is not None else l2
        # prehead初始化为空节点，要返回其next才是链表头结点
        # 单链表由其头结点确定
        return prehead.next
