"""
给定一个头结点为 root 的链表, 要求将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，可能有些部分为 null。
这k个部分应该按照在链表中出现的顺序输出，并且排在前面的部分的长度应该大于或等于后面的长度。
返回一个符合上述规则的链表的列表。
举例： 1->2->3->4, k = 5；结果 ：[ [1], [2], [3], [4], null ]

示例 2：
输入:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
解释:
输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        if x == None:
            return
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # 题目说了，头结点是root，不是首节点
        cur = root
        # 统计原链表的长度
        length = 0
        while cur:
            length += 1
            cur = cur.next
        # 平均长度
        avelen = int(length / k)
        # 余数
        extra = length % k
        # 结果中应有extra个长为avalen+1的链表，k-extra个长为avalen的链表。
        nodeList = []

        """先截取extra个长度为avelen + 1的链表"""
        avelen += 1
        while extra > 0:
            # 每趟循环前记录头指针
            head = root
            pre = None
            for i in range(avelen):
                pre = root
                root = root.next
            pre.next = None
            nodeList.append(head)
            extra -= 1

        """再截取k-extra个长度为avelen的链表"""
        k = k - (length % k)
        avelen -= 1
        if avelen == 0:
            while k > 0:
                nodeList.append(None)
                k -= 1
        while k > 0:
            if root:
                head = root
                pre = None
                for i in range(avelen):
                    pre = root
                    root = root.next
                pre.next = None
                nodeList.append(head)
            else:
                nodeList.append(None)
            k -= 1
        return nodeList


if __name__ == '__main__':
    list = [1, 2, 3, 4]
    node = ListNode(0)
    head = ListNode(0)
    head.next = node
    for i in range(len(list)):
        node.next = ListNode(0)
        node.next.val = list[i]
        node = node.next
    ans = Solution().splitListToParts(head.next.next, 5)
    print("最后列表的长度：", len(ans), ans)
    for i in range(len(ans)):
        print(ans[i].val, type(ans[i]))
