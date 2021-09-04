"""
给定一棵二叉树的前序（根、左、右）和中序（左、根、右）的打印结果，输出此二叉树按层（从左往右）打印结果。
例：
一棵二叉树前序：1 2 4 5 3；中序：4 2 5 1 3。
按层打印的结果则为：1 2 3 4 5。
"""


class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class S(object):
    def helper(self, preorder, preleft, preright, inleft, inright, mydict):
        if preleft > preright or inleft > inright:
            return
        rootval = preorder[preleft]
        rindex = mydict[rootval]
        root = TreeNode(rootval)
        root.left = self.helper(preorder, preleft + 1, rindex - inleft + preleft, inleft, rindex - 1, mydict)
        root.right = self.helper(preorder, rindex - inleft + preleft + 1, preright, rindex + 1, inright, mydict)
        return root

    def getTree(self, n, pre_order, in_order):
        mydict = {k: v for v, k in enumerate(in_order)}
        return self.helper(pre_order, 0, len(pre_order) - 1, 0, len(in_order) - 1, mydict)

    def getAns(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            num = len(queue)
            while num > 0:
                cur = queue.pop(0)
                res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                num -= 1
        return res


if __name__ == '__main__':
    n = int(input())
    order1 = list(map(int, input().split()))
    order2 = list(map(int, input().split()))
    print(order1, order2)
    s = S()
    root = s.getTree(n, order1, order2)
    ans = s.getAns(root)
    res = ""
    for ch in ans:
        res += str(ch) + " "
    print(res[:-1])
