"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
"""
"""
本题用动态规划，思路：
特判：
    根据数组的长度n判断数组是否可以被划分。如果 n<2，则不可能将数组分割成元素和相等的两个子集，因此直接返回False;
    计算整个数组的元素和 sum以及最大元素 maxNum。如果 sum是奇数，则不可能将数组分割成元素和相等的两个子集，因此直接返回False;
    如果sum 是偶数，则令target=sum/2，需要判断是否可以从数组中选出一些数字，使得这些数字的和等于target。
        如果 maxNum>target，则除了maxNum 以外的所有元素之和一定小于 target，因此不可能将数组分割成元素和相等的两个子集，直接返回False。
    
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # 特判
        if n < 2:
            return False
        # 求所有元素和
        allNums = sum(nums)
        if allNums % 2 == 1:
            return False
        # 设定目标值，要是能分，则两部分的和均为target
        target = allNums // 2
        # 求数组最大元素
        maxNums = max(nums)
        # 要是最大元素大于target，则不可分
        if maxNums > target:
            return False
        # 初始化DP数组
        # 其中 dp[i][j] 表示从数组的 [0,i]下标范围内选取若干个正整数（可以是 0 个），是否存在一种选取方案使得被选取的正整数的和等于 j。
        dp = []
        for i in range(n):
            temp = []
            for j in range(target + 1):
                temp.append(False)
            dp.append(temp)
        # 如果不选取任何正整数，则被选取的正整数等于 0。因此对于所有 0≤i<n，都有dp[i][0]=True。
        for i in range(n):
            dp[i][0] = True
        # 当i=0时，只有一个正整数nums[0]可以被选取，因此dp[0][nums[0]]=True
        dp[0][nums[0]] = True

        # 当 i>0 且 j>0 时
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        for i in range(n):
            print(dp[i])

        return dp[n-1][target]


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))
