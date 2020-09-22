"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例：
输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

    # 暴力毫无疑问超时
    def countSmaller2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = []
        for i in range(len(nums)):
            temp = nums[i:]
            index = 0
            for item in temp:
                if item < nums[i]:
                    index += 1
            count.append(index)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countSmaller(nums=[5, 2, 6, 1]))
