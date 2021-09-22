class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class S():
    def delKthNode(self, head, K):
        ans = LinkNode(0)
        ans.next = head
        cur = ans
        while K:
            cur = cur.next
            K -= 1
        cur.next = cur.next.next
        return ans.next


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    head = LinkNode(0)
    cur = head
    for num in nums:
        node = LinkNode(num)
        cur.next = node
        cur = cur.next
    cur.next = None
    s = S()
    ans = s.delKthNode(head.next, m-1)
    while ans:
        print(ans.val, end=" ")
        ans = ans.next
