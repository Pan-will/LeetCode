"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sumt: int
        :rtype: int
        """

        if not root:
            return 0
        ans = self.dfs(root, sum)
        ans_left = self.dfs2(root.left, sum)
        ans_right = self.dfs2(root.right, sum)
        return ans + ans_left + ans_right

    def dfs2(self, node, sum):
        if not node:
            return 0
        sum = sum - node.val
        ans = 1 if sum == 0 else 0
        return ans + self.dfs2(node.left, sum) + self.dfs2(node.right, sum)

    def pathSum2(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        self.count = 0
        myDict = {0: 1}

        def dfs(p, target, pathSum, myDict):
            if p:
                pathSum += p.val
                self.count += myDict.get(pathSum - target, 0)
                myDict[pathSum] = myDict.get(pathSum, 0) + 1
                dfs(p.left, target, pathSum, myDict)
                dfs(p.right, target, pathSum, myDict)
                myDict[pathSum] -= 1
        dfs(root, target, 0, myDict)
        return self.count
