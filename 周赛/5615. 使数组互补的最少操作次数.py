"""
给你一个长度为 偶数 n 的整数数组 nums 和一个整数 limit 。
每一次操作，你可以将 nums 中的任何整数替换为 1 到 limit 之间的另一个整数。

如果对于所有下标 i（下标从 0 开始），nums[i] + nums[n - 1 - i] 都等于同一个数，
则数组 nums 是 互补的 。例如，数组 [1,2,3,4] 是互补的，因为对于所有下标 i ，nums[i] + nums[n - 1 - i] = 5 。

返回使数组 互补 的 最少 操作次数。


示例 1：
输入：nums = [1,2,4,3], limit = 4
输出：1
解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）：
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。
"""


# 思路：用res统计对称位置的和，找出有几个是不一样的，即是答案。
class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        mydict = {}
        i, j = 0, n - 1
        while i < j:
            if nums[i] + nums[j] in mydict.keys():
                mydict[nums[i] + nums[j]] += 1
            else:
                mydict[nums[i] + nums[j]] = 1
            i += 1
            j -= 1
        mylist = sorted(mydict.items(), key=lambda x: x[1])
        return mylist[0][1]


if __name__ == '__main__':
    s = Solution()
    print(s.minMoves([1, 2, 2, 1], 4))
