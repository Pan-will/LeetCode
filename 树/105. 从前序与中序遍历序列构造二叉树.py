"""
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preindex = 0
        # 用字典存储中序序列中root的值与下标
        indict = {v: i for i, v in enumerate(inorder)}
        root = self.dg(0, len(preorder) - 1, preorder, inorder, indict)
        return root

    def dg(self, start, end, preorder, inorder, indict):
        if start <= end:
            # 利用字典：index = dict[val]
            rindex = indict[preorder[self.preindex]]
            self.preindex += 1
            root = TreeNode(inorder[rindex])
            root.left = self.dg(start, rindex - 1, preorder, inorder, indict)
            root.right = self.dg(rindex + 1, end, preorder, inorder, indict)
            return root

    """
    效率更高。时间复杂度空间复杂度都是O(n).
    """
    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 用字典存储中序序列中root的值与下标
        myDict = {v: i for i, v in enumerate(inorder)}
        return self.dg2(preorder, 0, len(preorder) - 1, 0, len(inorder) - 1, myDict)

    def dg2(self, preorder, preLeft, preRight, inLeft, inRight, myDict):
        if preLeft > preRight or inLeft > inRight:
            return
        rootVal = preorder[preLeft]
        rootIndex = myDict[rootVal]
        root = TreeNode(rootVal)
        root.left = self.dg2(preorder, preLeft + 1, rootIndex - inLeft + preLeft, inLeft, rootIndex-1, myDict)
        root.right = self.dg2(preorder, rootIndex - inLeft + preLeft + 1, preRight, rootIndex+1, preRight, myDict)
        return root


if __name__ == '__main__':
    s = Solution()
    s.buildTree2([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
