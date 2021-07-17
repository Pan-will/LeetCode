"""
输入：nums = [0,2,1,5,3,4]
输出：[0,1,2,4,5,3]
解释：数组 ans 构建如下：
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
"""


class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        return [nums[i] for i in range(len(nums))]


if __name__ == '__main__':
    s = Solution()
    print(s.buildArray([0, 2, 1, 5, 3, 4]))
