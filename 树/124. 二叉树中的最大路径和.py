"""
DFS

给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
该路径至少包含一个节点，且不一定经过根节点。

示例 1：
输入：[1,2,3]
       1
      / \
     2   3
输出：6

示例 2：
输入：[-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
输出：42
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # def __init__(self):
    #     self.maxsum = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxsum = float("-inf")
        maxsum = self.getGain(root, maxsum)
        return maxsum

    # 递归每个节点的贡献值
    def getGain(self, node, maxsum):
        if not node:
            return 0
        # 递归左右子树的贡献值，贡献值必须大于0才要
        leftGain = max(self.getGain(node.left), 0)
        rightGain = max(self.getGain(node.right), 0)
        # 更新贡献值=当前节点值+左节点+右节点
        newSum = node.val + leftGain + rightGain
        # 更新全局最大值
        maxsum = max(maxsum, newSum)
        # 返回该节点的最大贡献值
        return node.val + max(leftGain, rightGain)
