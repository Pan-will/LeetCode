class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 堆队列算法，比如优先队列
        import heapq
        pre = ListNode(-1)
        cur = pre
        # 优先队列
        head = []
        # 遍历所有链表
        for i in range(len(lists)):
            if lists[i]:
                # 将链表头结点放入优先队列中，放入头结点，就相当于放入了整个链表！！
                heapq.heappush(head, (lists[i].val, i))
                # 各链表首指针往后移动
                lists[i] = lists[i].next
        # 合并队列中已有的节点
        while head:
            # 取得节点值域，及其在对应链表中节点的下标位置
            # 由于优先队列的性质:heappop()的就是当前队列中最小元素
            val, index = heapq.heappop(head)
            # 构造节点并入结果链表
            cur.next = ListNode(val)
            # 指针往后顺移
            cur = cur.next
            # 若最小节点对应的链表不为空
            if lists[index]:
                # 将对应链表的下一个节点入队
                heapq.heappush(head, (lists[index].val, index))
                # 遍历该链表的指针往后顺移
                lists[index] = lists[index].next
        return pre.next
