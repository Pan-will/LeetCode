"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：
输入：
   1
    \
     3
    /
   2

输出：
1

解释：最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 所有节点非负；二叉搜索树中序是有序序列。
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 得到二叉树的中序序列
        midlist = self.mid_order(root)
        res = 9999999
        i, j = 0, 1
        while j < len(midlist):
            if midlist[j] - midlist[i] < res:
                res = midlist[j] - midlist[i]
            j += 1
            i += 1
        return res

    def mid_order(self, root):
        if not root:
            return []
        return self.mid_order(root.left) + [root.val] + self.mid_order(root.right)
