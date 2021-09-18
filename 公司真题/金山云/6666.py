class Solution:
    def getAns(self, nums):
        if len(nums) < 3:
            return 0

        nums.sort()

        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            # target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s % 3 == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 去重
                    while left < right:
                        left = left + 1
                        if nums[left - 1] != nums[left]: break
                    while left < right:
                        right = right - 1
                        if nums[right + 1] != nums[right]: break
                else:
                    right = right - 1
        # print(res)
        return len(res)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
s = Solution()
print(s.getAns(nums))
