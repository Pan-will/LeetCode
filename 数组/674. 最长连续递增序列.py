"""
给定一个未经排序的整数数组，找到最长且连续的的严格递增序列。

示例 1:
输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

示例 2:
输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums为空
        if len(nums) == 0:
            return 0
        # 存放各连续递增序列的长度，返回其最大值
        res = []
        # 记录各连续递增序列的长度
        size = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                size += 1
            else:
                res.append(size)
                # 重置递增序列的长度
                size = 1
        # 如果nums整体是个递增序列
        res.append(size)
        return max(res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLengthOfLCIS([1, 3, 5, 7]))
