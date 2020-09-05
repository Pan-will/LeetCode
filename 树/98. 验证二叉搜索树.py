"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        inorderList = self.inorder(root)
        i, j = 0, 1
        while j < len(inorderList):
            if inorderList[i] >= inorderList[j]:
                return False
            i += 1
            j += 1
        return True

    # 中序遍历，迭代法
    def inorder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        mid_stack = []
        ans = []
        cur = root
        while cur or mid_stack:
            while cur:
                mid_stack.append(cur)
                cur = cur.left
            temp = mid_stack.pop()
            ans.append(temp.val)
            cur = temp.right
        return ans
