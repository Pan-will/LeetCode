class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inOrder2(self, root):
        if not root: return []
        return self.inOrder2(root.left) + [root.val] + self.inOrder2(root.right)

    def inOrder(self, root):
        if not root: return []
        return self.inOrder(root.left) + [root] + self.inOrder(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return
        in1 = self.inOrder(root)
        in2 = sorted(in1, key=lambda x: x.val)
        err1, err2 = [in1[i] for i in range(len(in1)) if in1[i] != in2[i]]
        err1.val, err2.val = err2.val, err1.val


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    node2 = TreeNode(5)
    node3 = TreeNode(4)
    node4 = TreeNode(1)
    node5 = TreeNode(2)
    root.left = node2
    root.right = node3
    node2.left = node4
    node3.right = node5
    print(s.inOrder2(root))
    s.recoverTree(root)
    print(s.inOrder2(root))