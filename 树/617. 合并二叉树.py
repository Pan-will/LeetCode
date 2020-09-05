"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。
合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 递归
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        if t1 and not t2:
            return t1
        if not t1 and t2:
            return t2
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    # 迭代
    """
    思路：
        栈中的每个元素都会存放两个根节点，并且栈顶的元素表示当前需要处理的节点。
        在迭代的每一步中，取出栈顶的元素并把它移出栈，并将它们的值相加。
        随后分别考虑这两个节点的左孩子和右孩子：
            如果两个节点都有左孩子，那么就将左孩子入栈；
            如果只有一个节点有左孩子，那么将其作为第一个节点的左孩子；
            如果都没有左孩子，那么不用做任何事情。
            对于右孩子同理。
        最后返回第一棵树的根节点作为答案。
    """

    def mergeTrees2(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 如果两树有一个为空，则直接返回
        if not (t1 and t2):
            return t1 if not t2 else t2
        # 设栈
        stack = [[t1, t2]]
        while stack:
            node = stack.pop(0)
            if not node[0] or not node[1]:
                continue
            node[0].val += node[1].val
            # 考虑两树的左孩子
            if not node[0].left:
                node[0].left = node[1].left
            else:
                stack.append([node[0].left, node[1].left])
            # 考虑两树的右孩子
            if not node[0].right:
                node[0].right = node[1].right
            else:
                stack.append([node[0].right, node[1].right])
        return t1
