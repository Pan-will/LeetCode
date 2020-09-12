"""
发现二叉树很多题都是用BFS和DFS做，觉得有必要总结一套代码模板。
所谓模板只是方便套用架子，而不是生搬硬抄，随机应变做修改很重要。
"""

"""
BFS，用队列实现，特点是先进先出。
"""


class Solution():
    def BFS(self, root):
        # 特判：树根为空
        if not root:
            return []
        # 返回值list
        res = []
        # 设置队列，初始时根入队
        queue = [root]
        # 开始遍历，循环条件：队列不为空
        # 外层的while遍历树的层数
        while queue:
            # 获得当前队列的长度，即当前层节点的个数
            lenQueue = len(queue)
            # 内层for循环遍历当前层的所有节点
            for i in range(lenQueue):
                # 队首节点出队并读取其值域
                node = queue.pop(0)
                res.append(node.val)
                # 将出队节点的子树入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

    """
    前序遍历式DFS
    """

    # 迭代式
    def pre_DFS(self, root):
        # 特判：树根为空
        if not root:
            return []
        # 返回值
        res = []
        # 设置栈，特点是先进后出，初始时树根入栈
        # 用栈存储下一步可能访问的节点
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                # 栈是先进后出，所以先进栈右子树
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            cur = temp.right
        return res

    # 递归式
    def pre_DFS2(self, root):
        # 特判：树根为空
        if not root:
            return []
        # 返回值
        res = []
        res.append(root.val)
        res += self.pre_DFS2(root.left)
        res += self.pre_DFS2(root.right)
        return res

    """
    中序遍历式DFS
    """
    # 迭代式
    def mid_DFS(self, root):
        # 特判：树根为空
        if not root:
            return []
        # 返回值
        res = []
        # 设置栈，特点是先进后出，初始时树根入栈
        # 用栈存储下一步可能访问的节点
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            res.append(cur.val)
            temp = stack.pop()
            cur = temp.right
        return res

    # 递归式
    def mid_DFS2(self, root):
        # 特判：树根为空
        if not root:
            return []
        # 返回值
        res = []
        res += self.mid_DFS2(root.left)
        res.append(root.val)
        res += self.mid_DFS2(root.right)
        return res

    """
    后序遍历式DFS
    """
    # 迭代式
    def post_DFS(self, root):
        # 特判：树根为空
        if not root:
            return []
        # 返回值
        res = []
        cur = root
        stack = []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            temp = stack.pop()
            cur = temp.left
        return res[::-1]

    # 递归式
    def post_DFS2(self, root):
        # 特判：树根为空
        if not root:
            return []
        # 返回值
        res = []
        res += self.post_DFS2(root.left)
        res += self.post_DFS2(root.right)
        res.append(root.val)
        return res
