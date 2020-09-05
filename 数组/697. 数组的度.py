"""
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:
输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

思路：
1、nums转set去重，为newlist；
2、遍历newlist找出最大频数maxnum；
3、遍历newlist针对满足最大频数的元素ch，求其代表的连续子数组：
    a)从左往右遍历，找到第一个ch的下标low；
    b)从右往左遍历，找到第一个ch的下标high；
    将该子数组长度：high-low+1保存在res[ ]中；
4、返回min(res)。
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 去重
        newlist = list(set(nums))
        # 记录最大频数
        maxnum = 0
        # 返回min(res)
        res = []
        # 找出maxnum
        for ch in newlist:
            if nums.count(ch) > maxnum:
                maxnum = nums.count(ch)
        for ch in newlist:
            # 满足最大频数的元素
            if nums.count(ch) == maxnum:
                # 求相同度的子数组的长度
                low = nums.index(ch)
                high = -1
                for i in range(len(nums) - 1, -1, -1):
                    if nums[i] == ch:
                        high = i
                        break
                res.append(high - low + 1)
        return min(res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findShortestSubArray([1, 2, 2, 3, 1]))
