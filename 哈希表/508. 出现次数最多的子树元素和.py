"""
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

示例 1：
输入:
  5
 /  \
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例 2：
输入：
  5
 /  \
2   -5
返回 [2]，只有 2 出现两次，-5 只出现 1 次。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.mydict = {}

    # 1、dfs求每个节点的子树和，并用字典统计
    # 2、遍历字典，按values域的大小降序排：mylist = sorted(mydict.items(), key = lambda x: x[1], reverse=True)
    # 3、遍历mylist，res中append字典的第一个item的values域，要是后面的values域长度跟首item相同，则res继续append；
    # 4、return res
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        self.getTheTreeSum(root)
        print(self.mydict)
        mylist = sorted(self.mydict.items(), key=lambda x: x[1], reverse=True)
        maxsum = mylist[0][1]
        res = []
        for item in mylist:
            if item[1] == maxsum:
                res.append(item[0])
            else:
                break
        return res

    # dfs求每个节点的子树和
    def getTheTreeSum(self, root):
        temp = self.getCurSum(root)
        if temp in self.mydict.keys():
            self.mydict[temp] += 1
        else:
            self.mydict[temp] = 1
        if root.left:
            self.getTheTreeSum(root.left)
        if root.right:
            self.getTheTreeSum(root.right)

    # dfs求树节点的值域和，参数是根节点
    def getCurSum(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return node.val
        return self.getCurSum(node.left) + node.val + self.getCurSum(node.right)

if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(-3)
    root.left = node1
    root.right = node2

    s = Solution()

    print(s.findFrequentTreeSum(root))
