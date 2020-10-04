# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bfsList = self.BFS(root)
        for i, item in enumerate(bfsList):
            # 偶数层
            if i % 2 == 0:
                # 检查该层是否有偶数
                for j in item:
                    if j % 2 == 0:
                        return False
                # 检查是否递增
                if not self.isUp(item):
                    return False

            # 奇数层
            else:
                # 检查该层是否有偶数
                for j in item:
                    if j % 2 == 1:
                        return False
                # 检查是否递减
                if not self.isDown(item):
                    return False
        return True

    def BFS(self, root):
        # 特判：树根为空
        if not root:
            return []
        level_queue = []
        ans = []
        level_queue.append(root)
        while level_queue:
            num = len(level_queue)
            temp = []
            while num > 0:
                cur = level_queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    level_queue.append(cur.left)
                if cur.right:
                    level_queue.append(cur.right)
                num -= 1
            ans.append(temp)
        return ans

    # 检查是否递增
    def isUp(self, nums):
        if len(nums) < 2:
            return True
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] <= nums[slow]:
                return False
            slow += 1
            fast += 1
        return True

    # 检查是否递减
    def isDown(self, nums):
        if len(nums) < 2:
            return True
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] >= nums[slow]:
                return False
            slow += 1
            fast += 1
        return True
