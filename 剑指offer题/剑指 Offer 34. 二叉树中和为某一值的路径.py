"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]

算法流程：
pathSum(root, sum) 函数：
    初始化： 结果列表 res ，路径列表 path 。
    返回值： 返回 res 即可。

recur(root, tar) 函数：
    递推参数： 当前节点 root ，当前目标值 tar 。
    终止条件： 若节点 root 为空，则直接返回。
    递推工作：
    路径更新： 将当前节点值 root.val 加入路径 path ；
    目标值更新： tar = tar - root.val（即目标值 tar 从 sum 减至 00 ）；
    路径记录： 当 ① root 为叶节点 且 ② 路径和等于目标值 ，则将此路径 path 加入 res 。
    先序遍历： 递归左 / 右子节点。
    路径恢复： 向上回溯前，需要将当前节点从路径 path 中删除，即执行 path.pop() 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        road = []
        self.pre_order(root, sum, res, road)
        return res

    def pre_order(self, node, total, res, road):
        # 当前节点为空，直接return
        if not node:
            return
        # 否则将当前节点加入路径中
        road.append(node.val)
        # 目标值减掉当前节点的值
        total -= node.val
        # 当前节点是叶子、且和为目标值，则将路径加入外层list中
        if total == 0 and not node.left and not node.right:
            res.append(list(road))
        # 前序式递归当前节点的左右子树
        self.pre_order(node.left, total, res, road)
        self.pre_order(node.right, total, res, road)
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
    print(s.pathSum(root, 10))
