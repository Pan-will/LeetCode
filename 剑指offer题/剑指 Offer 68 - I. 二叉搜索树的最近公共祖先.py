# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 方法一，递归思路：
    #   当p,q都在root的右子树中时，递归root.right并返回；
    #   当p,q都在root的左子树中时，递归root.left并返回；
    #   返回值：最近公共祖先root。
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    # 方法二，迭代思路：
    # 先特判：
    #   当节点root为空时：return None;
    #   当p、q值域相同时，return p 或 return q;
    # 再遍历：
    #   如果，当p,q都在root的右子树中,则遍历至root.right：root = root.right;
    #   否则，当p,q都在root的左子树中,则遍历至root.left：root = root.left;
    #   否则，说明找到了最近公共祖先,则return root。
    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p.val == q.val:
            return p
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

    # 针对一般二叉树。
    # 先特判：
    #   当节点root为空时：return None;
    #   当p或q的值域等于root时，return root;
    # 再递归判断root的左、右子树；
    #   若左右子树都不为空：return root;
    #   若左真右假：return 左;
    #   若左假右真：return 右;
    #   否则，左右都为空：return None;
    def lowestCommonAncestor3(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # if p.val == q.val:
        #     return p
        if p.val == root.val or q.val == root.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None