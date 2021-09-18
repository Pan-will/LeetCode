class Solution(object):
    def __init__(self):
        self.res = []

    def getAns(self, candidates):
        # 特判
        if not candidates:
            return []
        candidates.sort()
        # 获取元素个数
        n = len(candidates)
        # 调用函数
        self.dfs(candidates, 1, n, 0, 0, [])
        return self.res

    def dfs(self, candidates, target, n, begin, temp_sum, temp):
        if temp_sum == target:
            self.res.append(temp)
            return
        for i in range(begin, n):
            # 超过目标值了，不符合
            if temp_sum + candidates[i] > target:
                break
            # 不能选相同的元素
            if i > begin and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target, n, i + 1, temp_sum + 1/candidates[i], temp + [candidates[i]])


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.getAns(nums))
