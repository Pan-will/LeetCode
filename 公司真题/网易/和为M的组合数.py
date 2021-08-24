# 思路：回溯
class Solution():
    def method(self, nums, m):
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        temp = []
        res = []
        visit = [0 for _ in range(n)]
        self.helper(m, nums, n, temp, res, visit)
        print(res)
        return len(res)

    def helper(self, tar, nums, n, temp, res, visit):
        if len(temp) == 2:
            if sum(temp) <= tar:
                if temp not in res:
                    res.append(temp)
        else:
            for i in range(n):
                if visit[i] == 0:
                    visit[i] = 1
                    self.helper(tar, nums, n, temp + [nums[i]], res, visit)
                    visit[i] = 0

if __name__ == '__main__':
    nums = input().split(" ")
    m = input()
    for i, digit in enumerate(nums):
        nums[i] = int(digit)
    m = int(m)
    print(m, nums)
    s = Solution()
    print(s.method(nums, m))
