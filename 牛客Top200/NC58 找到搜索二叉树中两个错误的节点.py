class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getmidorder(self, root):
        if not root:
            return None
        stack = []
        cur = root
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            res.append(temp.val)
            cur = temp.right
        print("中序：", res)
        return res

    def findError(self, root):
        # write code here
        if not root: return None
        mid1 = self.getmidorder(root)
        mid2 = sorted(mid1)
        print(mid2)
        ans = []
        for i, j in zip(mid1, mid2):
            if i != j:
                ans.append(j)
        return ans


if __name__ == '__main__':
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
    # n2.left = n4
    # n2.right = n5
    # n3.left = n6
    # n3.right = n7
    # n7.right = n8
    # n8.right = n9
    s = Solution()

    print(s.findError(root))
