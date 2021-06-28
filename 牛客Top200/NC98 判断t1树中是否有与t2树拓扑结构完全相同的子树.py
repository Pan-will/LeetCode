class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def midorder(self, root):
        if not root: return []
        return self.midorder(root.left) + [root.val] + self.midorder(root.right)

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

    def isContains(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        mid1 = self.inorder(root1)
        mid2 = self.inorder(root2)
        if mid2 in mid1:
            return True
        else:
            return False
