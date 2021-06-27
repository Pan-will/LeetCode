"""
两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。

例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差 取到 最大值 。

返回以这种方式取得的乘积差中的 最大值 。
"""


class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        nums.sort()  # 先升个序
        return nums[-1] * nums[-2] - nums[0] * nums[1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProductDifference(nums=[5, 6, 2, 7, 4]))
