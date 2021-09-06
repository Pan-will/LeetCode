class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param a ListNode类一维数组 指向这些数链的开头
# @return ListNode类
class Solution(object):
    def findAns(self, a):
        print("链表数量：", len(a))
        res = ListNode(0)
        head = res
        i = 0
        while 1:
            if i >= len(a):
                break
            cur = a[i]
            head.next = cur
            if cur.next:
                a.append(cur.next)
            i += 1
            head = head.next
        return res.next

    def getAns(self, a):
        count = len(a)  # 计数器，当前还有多少条非空链表
        print("链表数量：", count, a[0].val, a[-1].val)
        res = ListNode(0)
        head = res
        while count > 0:
            for i in range(count):  # 内层循环控制每次获取每个链表的头节点
                if a[i]:
                    node = ListNode(a[i].val)  # 不用原节点，直接构造同值新节点
                    head.next = node
                    head = head.next
                    a[i] = a[i].next  # 当前链表指针顺移
                    if not a[i]:  # 每次取完做判空，删除空链表提升效率
                        a.pop(i)  # 移除空链表
                        count -= 1  # 移除一条空链表，计数器减1
        return res.next

    def solve(self, a):
        n = len(a)  # 首先取到链表数量
        print("链表数量：", n)
        res = ListNode(0)
        head = res
        for i in range(n):
            if a[i]:
                head.next = a[i]
                head = head.next
                a[i] = a[i].next
        return res.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node10 = ListNode(10)
    node11 = ListNode(11)
    node12 = ListNode(12)
    node13 = ListNode(13)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10

    node11.next = node12
    node12.next = node13

    test = []
    test.append(node1)
    test.append(node5)
    test.append(node11)

    s = Solution()
    # head = s.solve(test)
    # head = s.getAns(test)
    head = s.findAns(test)
    while head:
        print(head.val)
        head = head.next
