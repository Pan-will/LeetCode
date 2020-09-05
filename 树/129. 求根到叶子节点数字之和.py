"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。

示例 1:
输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, 0)

    def dfs(self, root, sum):
        total = 0
        sum = sum*10 + root.val
        if not root.left and not root.right:
            return sum
        else:
            if root.left:
                total += self.dfs(root.left, sum)
            if root.right:
                total += self.dfs(root.right, sum)
            return total


if __name__ == '__main__':
    root = TreeNode(1)
    n10 = TreeNode(2)
    n11 = TreeNode(2)
    n20 = TreeNode(3)
    n21 = TreeNode(4)
    n22 = TreeNode(4)
    n23 = TreeNode(3)
    root.left = n10
    root.right = n11
    n10.left = n20
    n10.right = n21
    n11.left = n22
    n11.right = n23
    n20.left = None
    n20.right = None
    n21.left = None
    n21.right = None
    n22.left = None
    n22.right = None
    n23.left = None
    n23.right = None
    s = Solution()
    print(s.sumNumbers(root))
