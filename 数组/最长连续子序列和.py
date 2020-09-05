class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        l = len(array)
        dp = []
        dp.append(array[0])
        for i in range(1, l):
            dp.append(max(dp[i - 1] + array[i], array[i]))
        ans = dp[0]
        for item in dp:
            if item > ans:
                ans = item
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))
