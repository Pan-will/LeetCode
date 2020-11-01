"""
设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。

示例 1:
输入: nums = [5,6,5], target = 11
输出: [[5,6]]

示例 2:
输入: nums = [5,6,5,6], target = 11
输出: [[5,6],[5,6]]
"""


class Solution(object):
    # 双指针
    def pairSums2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = []
        i, j = 0, len(nums) - 1
        while i < j:
            temp = nums[i] + nums[j]
            if temp > target:
                j -= 1
            elif temp < target:
                i += 1
            else:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
        return res

    def pairSums(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        mydict = {}
        for i, item in enumerate(nums):
            if item in mydict.keys():
                mydict[item] += 1
            else:
                mydict[item] = 1
        print(mydict)
        res = []
        for item in nums:

            if target - item in mydict.keys() and mydict[item] > 0:
                mydict[item] -= 1
                if mydict[target - item] > 0:
                    res.append([item, target - item])
                    mydict[target - item] -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.pairSums2(nums=[5, 6, 5, 6], target=11))
