class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findAllPaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        road = []
        self.pre_DFS(root, res, road)
        return res

    # 前序式DFS——用list返回二叉树的所有路径
    # 注意每趟递归前要将当前节点pop()掉
    def pre_DFS(self, node, res, road):
        # 当前节点为空，直接return
        if not node:
            return
        # 否则将当前节点加入路径中
        road.append(node.val)
        # 当前节点是叶子则将路径加入外层list中
        if not node.left and not node.right:
            res.append(list(road))
        # 前序式递归当前节点的左右子树
        self.pre_DFS(node.left, res, road)
        self.pre_DFS(node.right, res, road)
        # 每趟递归前将当前节点pop()
        road.pop()
        # 返回外层list
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    node2 = TreeNode(2)
    node7 = TreeNode(7)
    node5 = TreeNode(5)
    root.left = node2
    root.right = node7
    node2.right = node5
    s = Solution()
    print(s.findAllPaths(root))
