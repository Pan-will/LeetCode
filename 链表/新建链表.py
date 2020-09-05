# 链表节点类
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


# 链表类，生成链表以及定义相关方法
class LinkList(object):
    # 生成链表，这里使用list来生成
    def create(self, valList):
        """
        :type valList: list
        :rtype: ListNode
        """
        node = ListNode(0)
        head = ListNode(0)
        head.next = node
        for i in range(len(valList)):
            node.next = ListNode(0)
            node.next.val = valList[i]
            node = node.next
        return head.next

    # 遍历显示
    def printLink(self, head):
        """
        :type head: ListNode
        :rtype: None
        """
        ans = head.next
        while ans:
            print(ans.val, end=' ')
            ans = ans.next
        # 回车换行
        print()

    # 链表判空
    def isEmpty(self, head):
        """
        :type head: ListNode
        :rtype: Boolean
        """
        # 若头指针为空，即链表为空，返回True; 否则返回False
        return True if not head else False

    # 取链表长度: 不算头结点
    def size(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans = head.next
        size = 0
        while ans:
            size += 1
            ans = ans.next
        return size

    # 根据索引取节点值域
    def getItem(self, head, index):
        """
        :type head: ListNode
        :type index: int
        :rtype: int
        """
        p = head.next
        count = 0
        while count != index:
            p = p.next
            count += 1
        return p.val

    # 根据索引设值
    def setItem(self, head, index, val):
        """
        :type head: ListNode
        :type index: int
        :type val: int
        :rtype: None
        """
        p = head
        count = -1
        while count < index - 1:
            p = p.next
            count += 1
        p.val = val

    # 单链表快速排序
    def quickSort(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        ans = ListNode(0)
        ans.next = head
        return self.sort(ans, None)
    def sort(self, head, end):
        if head == end or head.next == end or head.next.next == end:
            return head
        tpmHead = ListNode(0)
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
        self.sort(head, poi)
        self.sort(poi, end)
        return head.next

    # 单链表归并排序
    def mergeSort(self, head):
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
        right = self.mergeSort(slow.next)
        # 断开左右两部分链表
        slow.next = None
        # 对左半部分归并排序
        left = self.mergeSort(head)
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


if __name__ == "__main__":
    # 数组/列表，存放链表节点的值域
    li = [4, 2, 5, 3, 7, 9, 1, 0]
    myLink = LinkList()
    # 生成单链表
    head = myLink.create(li)
    # 打印链表长度
    # print("长度：", myLink.size(head))
    # 判空
    # print("判空：", myLink.isEmpty(head))
    # 单链表快速排序（升序），不稳定排序算法
    print("原序：", end=' ')
    myLink.printLink(head)
    # ansQuick = myLink.quickSort(head)
    # print("快排升序：", end=' ')
    # myLink.printLink(ansQuick)
    # 单链表归并排序（升序），稳定排序算法
    ansMerge = myLink.mergeSort(head)
    print("归并升序：", end=' ')
    myLink.printLink(ansMerge)
