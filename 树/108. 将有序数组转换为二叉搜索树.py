# encoding="utf-8"
"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 很奇怪，本题同样的代码用python提交过不了，用python3就可以。
class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    def sortedArrayToBST2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def createBST(start, end):
            if start > end:
                return None
            midpos = (end + start) // 2
            root = TreeNode(nums[midpos])
            root.left = createBST(start, midpos - 1)
            root.right = createBST(midpos + 1, end)
            return root

        return createBST(0, len(nums) - 1)

    # 迭代法，层序遍历
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level_queue = []
        ans = []
        level_queue.append(root)
        while level_queue:
            num = len(level_queue)
            while num > 0:
                cur = level_queue.pop(0)
                ans.append(cur.val)
                if cur.left:
                    level_queue.append(cur.left)
                if cur.right:
                    level_queue.append(cur.right)
                num -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    root = s.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(s.levelOrder(root))
