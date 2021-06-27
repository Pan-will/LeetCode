"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。
如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

示例 1:
输入:
    2
   / \
  2   5
     / \
    5   7
输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        temp = []
        stack = [root]
        while stack:
            sizestack = len(stack)
            for i in range(sizestack):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        temp.sort()
        extra = temp[0]
        for i in temp:
            if i != extra:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    node2 = TreeNode(6)
    node3 = TreeNode(5)
    # node4 = TreeNode(5)
    # node5 = TreeNode(6)
    # node6 = TreeNode(6)
    root.left = node2
    root.right = node3
    # node2.right = node4
    # node3.left = node5
    # node5.right = node6
    print(s.findSecondMinimumValue(root))
