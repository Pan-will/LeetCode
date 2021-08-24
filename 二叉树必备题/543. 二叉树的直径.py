"""
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node.left and not node.right:
            return 0
        ll = 0 if not node.left else self.dfs(node.left) + 1
        rr = 0 if not node.right else self.dfs(node.right) + 1
        self.res = max(self.res, ll + rr)
        return max(ll, rr)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    print(s.diameterOfBinaryTree(root))
