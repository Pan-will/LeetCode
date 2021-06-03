# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类

class Solution:
    # 双指针法：p1和p2分别从两个链表的头结点开始，当一个遍历完成则从另一链表的头结点重新遍历，
    # 如此，当两个指针相遇时即目标节点。
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = pHead2 if not p1 else p1.next
            p2 = pHead1 if not p2 else p2.next
        return p1

