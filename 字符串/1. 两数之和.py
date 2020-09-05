"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
输入：[2, 7, 11, 15], 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

思路：双指针；
每一趟遍历的前提：i<j;
i指针从前往后，j指针从后往i;
遇到满足条件的终止遍历并返回i、j;
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 初始化双指针
        i, j = 0, len(nums) - 1
        result = []
        for i in range(0, len(nums)-1):
            while i < j:
                if i < j and target - nums[i] != nums[j]:
                    j -= 1
                elif i < j and target - nums[i] == nums[j]:
                    result.append(i)
                    result.append(j)
                    return result
            # 重置j指针：每一趟遍历j均从最后往前走
            j = len(nums)-1
            continue
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
