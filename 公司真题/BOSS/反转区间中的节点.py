class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class S(object):
    def revPart(self, head):
        if not head:
            return None
        res = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = res
            res = cur
            cur = temp
        return res

    def findAns(self, head, m, n):
        if not head or n < m:
            return None
        if m == n:
            return head
        # 先找到第m个元素
        res = LinkNode(0)
        res.next = head
        l, r = res, res
        pre = l
        while m > 0 and l:
            pre = l
            l = l.next
            m -= 1
        while n > 0:
            r = r.next
            n -= 1
        tem_r = r.next
        r.next = None
        pre.next = None
        new_head = self.revPart(l)

        pre.next = new_head
        l.next = tem_r
        return res.next

    def showLink(self, head):
        if not head:
            print("link is None")
        while head:
            print(head.val, end=" ")
            head = head.next


if __name__ == '__main__':
    m, n = 1, 1
    nums = [1, 2, 3, 4, 5, 6]
    head = LinkNode(0)
    cur = head
    for num in nums:
        node = LinkNode(num)
        cur.next = node
        cur = cur.next
    cur.next = None
    s = S()

    ans = s.findAns(head.next, m, n)
    s.showLink(ans)
