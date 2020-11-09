"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。

输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
"""


# Definition for a Node.
class Node:
    # 新型链表节点，有值域、next指针域、random指针域
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        self.visitHash = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 特判
        if not head:
            return None
        if head in self.visitHash:
            return self.visitHash[head]
        node = Node(head.val, None, None)
        self.visitHash[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node



    # 报错：Random pointer of node with label 13 points to a node from the original list.
    # 这才意识到本题的妙处呢，哈哈哈
    def copyRandomList2(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        pre = Node(-1, None, None)
        myhead = pre
        while head:
            node = Node(-1, None, None)
            node.val = head.val
            node.next = head.next
            node.random = head.random
            pre.next = node
            pre = pre.next
            head = head.next
        return myhead.next


"""
测试打印结果：
(7, <__main__.Node instance at 0x7f79ccb9fe10>, None)
(13, <__main__.Node instance at 0x7f79ccb9fe60>, <__main__.Node instance at 0x7f79ccb9fd70>)
(11, <__main__.Node instance at 0x7f79ccb9feb0>, <__main__.Node instance at 0x7f79ccb9ff00>)
(10, <__main__.Node instance at 0x7f79ccb9ff00>, <__main__.Node instance at 0x7f79ccb9fe60>)
(1, None, <__main__.Node instance at 0x7f79ccb9fd70>)
"""
if __name__ == '__main__':
    nodes = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    pre = Node(-1,None,None)
    head = pre
    for i,item in enumerate(nodes):
        # print(item)
        node = Node(item[0], i+1 if i<len(nodes) else None, item[1])
        pre.next = node
        pre = pre.next
    s = Solution()
    print(s.copyRandomList(head.next))



