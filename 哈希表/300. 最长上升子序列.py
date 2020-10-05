"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
"""


class Solution(object):
    # 正向遍历,如果nums中有负数就不对
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        ans = 0
        temp = [[] for _ in nums]
        for i in range(len(nums) - 1):
            count = 0
            for j in range(ans):
                if nums[i] < max(temp[j]):
                    count += 1
                else:
                    break
            temp[count].append(nums[i])
            if count == ans:
                ans += 1
        return ans

    # 反向遍历
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        ans = 0
        s = [[] for _ in nums]
        for i in range(len(nums) - 1, -1, -1):
            count = 0
            for j in range(ans):
                if nums[i] < max(s[j]):
                    count += 1
                else:
                    break
            s[count].append(nums[i])
            if count == ans:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
