"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    # 测试用例过不了：[0]，预期输出是：[0,#]，实际输出是：[]
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root or not root.left:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    # 层序遍历
    def connect2(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = [root]
        # while 循环迭代的是树的层级。
        while queue:
            l = len(queue)
            # 内部的 for 循环迭代的是同一层的所有节点
            for i in range(l):
                node = queue.pop(0)
                # 由于可以访问同一层级的所有节点，因此能够建立 next 指针连接。
                if i < l - 1:
                    node.next = queue[0]
                """
                for 循环弹出一个节点时，同时把它的左孩子节点和右孩子节点依次加入队列。
                因此队列中每个层级的元素也是顺序存储的。可以通过已有的顺序建立 next 指针。
                """
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    # 层序遍历
    def connect3(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        q, s = [root], []
        while q:
            while q:
                node = q.pop(0)
                if q:
                    node.next = q[0]
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
            q, s = s, q
        return root
