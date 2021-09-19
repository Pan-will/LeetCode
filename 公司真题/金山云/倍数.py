"""
现在给你N个正整数，从中选取3个数字的和，刚好能够组成M的倍数。
请问存在多少种不同的选取方案？
相同的一组数如果次序不同只能算做一种方案，不同位置的相同数字需当做同一个数字看待。
例如一组数字[2,3,3,4]，从中选取3个数字的和来组成3的倍数，只存在一种方案(2,3,4)。

思路：回溯吧。
"""


class Solution(object):
    def getAns(self, nums):
        # 特判
        if not nums:
            return
        # 取原数组长度
        n = len(nums)
        # 设置访问标记数组，初始值均为0
        visit = [0 for _ in range(n)]
        temp = []
        res = []
        self.dfs(nums, n, temp, visit, res)
        return len(res)

    def dfs(self, nums, n, temp, visit, res):
        if len(temp) == 3 and sum(temp) % 3 == 0:
            temp.sort()
            if temp not in res:
                res.append(temp)
        else:
            for i in range(n):
                if not visit[i]:
                    visit[i] = 1
                    self.dfs(nums, n, temp + [nums[i]], visit, res)
                    visit[i] = 0


n, m = map(int, input().split())
nums = list(map(int, input().split()))
s = Solution()
print(s.getAns(nums))
