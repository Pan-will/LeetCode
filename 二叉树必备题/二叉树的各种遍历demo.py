class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序
def preorder(root):
    if not root:
        return []
    stack = []
    res = []
    cur = root
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        temp = stack.pop()
        cur = temp.right
    return res


# 中序
def inorder(root):
    if not root:
        return []
    stack = []
    res = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        temp = stack.pop()
        res.append(temp.val)
        cur = temp.right
    return res


# 后序
def postorder(root):
    if not root:
        return []
    stack = []
    res = []
    cur = root
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.right
        temp = stack.pop()
        cur = temp.left
    return res[::-1]


# 层序
def levelorder(root):
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


# 锯齿形层序遍历
def zhiLevelOrder(root):
    if not root:
        return []
    res = []
    queue = [root]
    i = 0
    while queue:
        num = len(queue)
        temp = []
        while num > 0:
            cur = queue.pop(0)
            temp.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
            num -= 1
        if i % 2 == 0:
            res += temp
        else:
            res += temp[::-1]
        i += 1
    return res


# 寻找二叉树两个节点的最近公共祖先
def findFather(root, p, q):
    if not root: return None
    if p.val == root.val or q.val == root.val: return root
    left = findFather(root.left, p, q)
    right = findFather(root.right, p, q)
    if left and right:
        return root
    elif left and not right:
        return left
    elif not left and right:
        return right
    else:
        return None


# 判断平衡二叉树
def isBalance(root):
    if not root:
        return True
    leftDeep = getDeep(root.left)
    rightDeep = getDeep(root.right)
    resLeft = isBalance(root.left)
    resRight = isBalance(root.right)
    if resLeft and resRight and abs(leftDeep - rightDeep) <= 1:
        return True
    else:
        return False


# 递归求二叉树的高度
def getDeep(root):
    if not root: return 0
    leftdeep = getDeep(root.left)
    rightdeep = getDeep(root.right)
    return leftdeep + 1 if leftdeep > rightdeep else rightdeep + 1


# 判断是否完全二叉树
def judgeComplete(root):
    if not root: return True
    queue = [root]
    h = 0
    while queue:
        num = len(queue)
        temp = []
        while num > 0:
            cur = queue.pop(0)
            temp.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            num -= 1
        if len(temp) != 2 ** h: return False
        h += 1
    return True


root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n7.right = n8
n8.right = n9
print("前序遍历：", preorder(root))
print("中序遍历：", inorder(root))
print("后序遍历：", postorder(root))
print("层序遍历：", levelorder(root))
print("之字形遍历：", zhiLevelOrder(root))
print("5和7的最新公共祖先是：", findFather(root, n5, n6).val)
print("root树的高度为：", getDeep(root))
print("root是不是平衡树？", isBalance(root))
print("root是不是完全二叉树？", judgeComplete(root))
