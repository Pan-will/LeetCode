"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
提示：如果众数超过1个，不需考虑输出顺序.
例如：
给定 BST [1,null,2,2],
   1
    \
     2
    /
   2
返回[2]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    思路：
        1、用字典记录每个几点出现的次数：mydict[node.val]；
        2、将mydict{}根据value降序；
        3、考虑众数不止一个，所以遍历items(),跟字典中第一个value域相等的都放到ans[]中返回。
    """

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # 返回值
        ans = []
        # 定义字典记录每个节点出现的次数
        mydict = {}
        # 调用DFS函数统计节点次数
        self.dfs(root, mydict)
        # sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        maxIndex = max(mydict.values())
        for k, v in mydict.items():
            if v == maxIndex:
                ans.append(k)
        return ans

    def dfs(self, node, mydict):
        if not node:
            return
        else:
            mydict[node.val] = mydict[node.val] + 1 if node.val in mydict.keys() else 1
            self.dfs(node.left, mydict)
            self.dfs(node.right, mydict)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    node2 = TreeNode(1)
    node3 = TreeNode(1)
    node4 = TreeNode(5)
    node5 = TreeNode(6)
    node6 = TreeNode(6)
    root.left = node2
    root.right = node3
    node2.right = node4
    node3.left = node5
    node5.right = node6
    print(s.findMode(root))
