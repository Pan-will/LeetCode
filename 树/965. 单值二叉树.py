"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。

示例 1：
输入：[1,1,1,1,1,null,1]
输出：true
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return True
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        return self.dfs(node.left) and self.dfs(node.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    node2 = TreeNode(1)
    node3 = TreeNode(1)
    node4 = TreeNode(1)
    node5 = TreeNode(1)
    node6 = TreeNode(6)
    root.left = node2
    root.right = node3
    node2.right = node4
    node3.left = node5
    node5.right = node6
    print(s.isUnivalTree(root))
