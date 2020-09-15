"""
实现一个函数，检查一棵二叉树是否为二叉搜索树。
示例 1:
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
    # 思路：BST的中序遍历应该是一个有序序列
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        midList = self.midOrder(root)
        # 双指针验证是不是有序序列
        i, j = 0, 1
        while j < len(midList):
            if midList[i] >= midList[j]:
                return False
            i += 1
            j += 1
        return True

    # 中序遍历，递归法
    def midOrder(self, root):
        if not root:
            return []
        res = []
        res += self.midOrder(root.left)
        res.append(root.val)
        res += self.midOrder(root.right)
        return res

    # 中序遍历，迭代法
    def mid_order(self,root):
        if not root:
            return []
        res = []
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            res.append(temp.val)
            cur = temp.right
        return res

