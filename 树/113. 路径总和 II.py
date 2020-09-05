"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        self.dfs(root, sum, ans, [])
        return ans

    def dfs(self, root, target, ans, temp):
        if root:
            temp.append(root.val)
            target -= root.val
            left = self.dfs(root.left, target, ans, temp)
            right = self.dfs(root.right, target, ans, temp)
            if not left and not right and target == 0:
                ans.append(temp + [])
            temp.pop()
            return True

    # 法二
    def pathSum2(self, root, sumt):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        stack = [(root, [root.val])]
        while stack:
            node, temp = stack.pop()
            if not node.left and not node.right and sum(temp) == sumt:
                ans.append(temp)
            if node.left:
                stack.append((node.left, temp + [node.left.val]))
            if node.right:
                stack.append((node.right, temp + [node.right.val]))
        return ans[::-1]


if __name__ == '__main__':
    root = TreeNode(5)
    n11 = TreeNode(4)
    n12 = TreeNode(8)
    n21 = TreeNode(11)
    n23 = TreeNode(13)
    n24 = TreeNode(4)
    n31 = TreeNode(7)
    n32 = TreeNode(2)
    n37 = TreeNode(5)
    n38 = TreeNode(1)
    root.left = n11
    root.right = n12
    n11.left = n21
    n11.right = None
    n12.left = n23
    n12.right = n24
    n21.left = n31
    n21.right = n32
    n23.left = None
    n23.right = None
    n24.left = n37
    n24.right = n38
    n31.left = None
    n31.right = None
    n32.left = None
    n32.right = None
    n37.left = None
    n37.right = None
    n38.left = None
    n38.right = None
    s = Solution()
    print(s.pathSum2(root, 32))
