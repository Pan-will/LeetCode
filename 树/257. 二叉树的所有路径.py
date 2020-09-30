"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        pathList = []
        if root.left:
            pathList += self.binaryTreePaths(root.left)
        if root.right:
            pathList += self.binaryTreePaths(root.right)
        for index, path in enumerate(pathList):
            pathList[index] = str(root.val) + "->" + path
        return pathList

    # 思路：用前序式DFS，从root到叶子。
    def binaryTreePaths2(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        return self.pre_DFS(root, res, "")

    def pre_DFS(self, root, res, road):
        if root:
            road += str(root.val)
            if not root.left and not root.right:
                res.append(road)
            else:
                road += '->'
                self.pre_DFS(root.left, res, road)
                self.pre_DFS(root.right, res, road)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    root.left = node2
    root.right = node3
    node2.right = node5
    s = Solution()
    print(s.binaryTreePaths2(root))
