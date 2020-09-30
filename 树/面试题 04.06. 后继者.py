"""
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:

输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        res = self.mid_Order(root)
        if len(res) <= 1:
            return None
        if p == res[-1]:
            return None
        return res[res.index(p) + 1]

    def mid_Order(self, root):
        if not root:
            return []
        return self.mid_Order(root.left) + [root] + self.mid_Order(root.right)


if __name__ == '__main__':
    root = TreeNode(2)
    node1 = TreeNode(1)
    root.left = node1
    s = Solution()
    print(s.inorderSuccessor(root, node1))
