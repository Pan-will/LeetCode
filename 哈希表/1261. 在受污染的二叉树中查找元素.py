"""
给出一个满足下述规则的二叉树：
root.val == 0
如果 treeNode.val == x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 1
如果 treeNode.val == x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x + 2
现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。

请你先还原二叉树，然后实现 FindElements 类：
FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。
bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。

示例 1：

输入：
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
输出：
[null,false,true]
解释：
FindElements findElements = new FindElements([-1,null,-1]);
findElements.find(1); // return False
findElements.find(2); // return True
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements(object):
    # treeNode.left.val == 2 * x + 1
    # treeNode.right.val == 2 * x + 2
    # 先dfs
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.mylict = []
        self.recover(root, 0)

    def recover(self, root, flag):
        if flag == 0:
            root.val = 0
            flag = 1
        self.mylict.append(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1
            self.recover(root.left, flag)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.recover(root.right, flag)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        print(self.mylict)
        if target in self.mylict:
            return True
        else:
            return False


if __name__ == '__main__':
    root = TreeNode(-1)
    # node1 = TreeNode(-1)
    node2 = TreeNode(-1)
    # node3 = TreeNode(-1)
    # node4 = TreeNode(-1)
    # node5 = TreeNode(-1)
    # node6 = TreeNode(-1)
    # root.left = node1
    root.right = node2
    # node1.left = node3
    # node1.right = node4
    # node2.left = node5
    # node2.right = node6

    s = FindElements(root)

    print(s.find(1), s.find(2))
