class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.ritht = None


class S(object):
    # 层序遍历
    def levelOrder(self, root):
        if not root: return None
        queue = [root]
        res = []
        while queue:
            temp = []
            l = len(queue)
            for _ in range(l):
                cur = queue.pop()
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(temp)
        return res

    # 求树高
    def getHigh(self, root):
        if not root: return 0
        lHigh = self.getHigh(root.left)
        rHigh = self.getHigh(root.right)
        return 1 + lHigh if lHigh > rHigh else rHigh + 1

    # 判断平衡树
    def isBanlance(self, root):
        if not root: return True
        lHigh = self.getHigh(root.left)
        rHigh = self.getHigh(root.right)
        lRes = self.isBanlance(root.left)
        rRes = self.isBanlance(root.right)
        if lRes and rRes and abs(lHigh - rHigh) <= 1:
            return True
        else:
            return False

    # 判断对称性
    def isDuicheng(self, root):
       if not root: return True
       return self.helper(root.left, root.right)
    def helper(self, rleft, rright):
        if not rleft and not rright: return True
        if not rleft and rright: return False
        if rleft and not rright: return False
        if rleft.val != rright.val: return False
        return self.helper(rleft.left, rright.right) and self.helper(rleft.right, rright.left)

    def getParent(self, root, p, q):
        if not root: return None
        if p.val == root.val or q.val == root.val: return root
        l = self.getParent(root.left, p, q)
        r = self.getParent(root.right, p, q)
        if l and r: return root
        elif l and not r: return l
        elif not l and r: return r
        else:
            return None
