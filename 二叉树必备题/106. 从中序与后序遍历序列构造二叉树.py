"""
根据一棵树的中序遍历与后序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。

例如，给出
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 用字典存储中序序列中root的值与下标
        myDict = {v: i for i, v in enumerate(inorder)}
        return self.dg(0, len(inorder) - 1, postorder, 0, len(postorder) - 1, myDict)

    def dg(self, inLeft, inRight, postorder, postLeft, postRight, myDict):
        if inLeft > inRight or postLeft > postRight:
            return
        rootVal = postorder[postRight]
        rootIndex = myDict[rootVal]
        root = TreeNode(rootVal)
        root.left = self.dg(inLeft, rootIndex - 1, postorder, postLeft, rootIndex - 1 - inLeft + postLeft, myDict)
        root.right = self.dg(rootIndex + 1, inRight, postorder, rootIndex - inLeft + postLeft, postRight - 1, myDict)
        return root
