"""
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
你可以返回满足此条件的任何数组作为答案。

示例：
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 根据元素是否为偶数排列
        return sorted(A, key=lambda num: num % 2 == 0)

    def sortnumsrrayByParity2(self, nums):
        if not nums:
            return None
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0 and nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i] % 2 == 0 and nums[j] % 2 != 1:
                j -= 1
                continue
            elif nums[i] % 2 != 0 and nums[j] % 2 == 1:
                i += 1
                continue
            elif nums[i] % 2 == 1 and nums[j] % 2 == 0:
                i += 1
                j -= 1
                continue
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArrayByParity2([6, 1, 2, 4]))
