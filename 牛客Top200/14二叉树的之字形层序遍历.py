class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans = []
        queue = [root]
        # 奇偶层标志
        sym = 0
        while queue:
            l = len(queue)
            temp = []
            for i in range(l):
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if sym % 2 == 0:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            sym += 1
        return ans
