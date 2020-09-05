"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
 
提示：节点值的范围在32位有符号整数范围内。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        ans = []
        queue = [root]
        # 外层while遍历的是树的层数
        while queue:
            temp = []
            l = len(queue)
            # 内层for遍历的是每层中的节点数
            for i in range(l):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(temp, l)
            # "/"符号两边只要有一个float类型，结果自动取float类型！！！
            ans.append(sum(temp)/float(l))
        return ans