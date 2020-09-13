"""
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # 用字典记录每个节点的父节点、以及该节点的深度（从0计）
        parent = {}
        depth = {}
        self.dfs(parent, depth, root, None)
        # 堂兄弟：不同父节点，但所处层数要相同
        return parent[x] != parent[y] and depth[x] == depth[y]

    def dfs(self, parent, depth, node, par=None):
        if node:
            # 记录当前节点的深度 = 父节点的深度+1，要是父节点不存在，则当前节点深度为0
            depth[node.val] = 1 + depth[par.val] if par else 0
            # 记录当前节点的父节点，若当前节点为根节点，则其父节点为None
            parent[node.val] = par
            # 递归左右子树
            self.dfs(parent, depth, node.left, node)
            self.dfs(parent, depth, node.right, node)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    root.left = node2
    root.right = node3
    node2.right = node4
    node3.left = node5
    node5.right = node6
    print(s.isCousins(root, 4, 6))
