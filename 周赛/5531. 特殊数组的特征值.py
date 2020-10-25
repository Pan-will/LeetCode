"""
给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。

注意： x 不必 是 nums 的中的元素。

如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。



示例 1：

输入：nums = [3,5]
输出：2
解释：有 2 个元素（3 和 5）大于或等于 2 。
"""


class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 升排排一下
        nums.sort()
        for i in range(1, len(nums)+1):
            tempnum = 0
            for j, item in enumerate(nums):
                if item >= i:
                    tempnum += 1
            if tempnum == i:
                return tempnum
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.specialArray([3, 5]))
