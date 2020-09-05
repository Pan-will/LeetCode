"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 方法一：深搜
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.dfs(root, 0, ans)
        return ans

    def dfs(self, root, h, ans):
        if root:
            if h == len(ans):
                ans.append(root.val)
            # 不同于先序遍历（左视图同先序），
            # 右视图每一层要从右往左访问，这样可以保证每层第一个访问的节点即是所需节点。
            self.dfs(root.right, h + 1, ans)
            self.dfs(root.left, h + 1, ans)
        return ans

    # 方法二：广搜
    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            qsize = len(queue)
            for i in range(qsize):
                # 队列先进先出，而pop()默认是出最后进来的元素
                # 所以一定要加上下标0
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == qsize-1:
                    ans.append(node.val)
        return ans
