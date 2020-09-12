"""
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # BFS
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        res = []
        stack = [root]
        while stack:
            sizestack = len(stack)
            for i in range(sizestack):
                node = stack.pop(0)
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        # 要返回的是第k大，所以降序排；若是第k小，则升序排
        res.sort(reverse=True)
        return res[k - 1]

    # DFS：二叉搜索树的中序遍历就是有序序列。
    def kthLargest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        res = self.mid_DFS(root)
        return res[len(res) - k]

    def mid_DFS(self, root):
        # 特判：树根为空
        if not root:
            return []
        # 返回值
        res = []
        res += self.mid_DFS(root.left)
        res.append(root.val)
        res += self.mid_DFS(root.right)
        return res
