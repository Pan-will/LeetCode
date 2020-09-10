"""
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

 

示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # 获取树的中序序列
        res = self.mid_DFS(root)
        return self.CreateTree(res)

    # DFS中序遍历二叉树
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

    # 构造二叉树
    def CreateTree(self,res):
        # 单边树的高度
        level = len(res)
        ans = root = TreeNode(0)
        poi = 0
        while level>poi:
            root.right = TreeNode(res[poi])
            root.left = None
            root = root.right
            poi += 1
        return ans.right
