"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 
注意:
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
"""


class Solution(object):
    # 遍历nums，每一趟遍历k个元素求和s时，将s清零，最后会超时。
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res = 0
        # 处理nums长度不大于k的情况
        if len(nums) <= k:
            for i in range(len(nums)):
                res += nums[i]
            return res / float(k)
        i, j = 0, k - 1
        while j < len(nums):
            s = 0
            for index in range(i, j + 1):
                s += nums[index]
            if res <= s:
                res = s
            i += 1
            j += 1
        return res / float(k)

    # 遍历nums，每一趟遍历k个元素求和s时，采用去头加尾的办法。
    def findMaxAverage2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        temp = sum(nums[:k])
        res = temp
        for i in range(k, len(nums)):
            # 去头加尾
            temp = temp - nums[i - k] + nums[i]
            res = max(res, temp)
        return res / float(k)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxAverage2([-1], 1))
