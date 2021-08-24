# 思路：回溯
class Solution():
    def method(self, nums):
        n = len(nums)
        if n < 2:
            return n
        if n == 2:
            if nums[0] == nums[1]:
                return n
            else:
                return 3
        if nums[0] > nums[-1] or nums[0] > nums[1]:
            zhis = [2]  # 存放每个孩子分几张纸
        else:
            zhis = [1]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                zhis.append(zhis[i - 1] + 1)
            elif i + 1 < len(nums) and nums[i] < nums[i - 1] and nums[i] > nums[i + 1]:
                zhis.append(zhis[i - 1])
            else:
                zhis.append(1)
        print(zhis)
        return sum(zhis)


if __name__ == '__main__':
    nums = input().split(" ")
    for i, digit in enumerate(nums):
        nums[i] = int(digit)
    s = Solution()
    print(s.method(nums))
