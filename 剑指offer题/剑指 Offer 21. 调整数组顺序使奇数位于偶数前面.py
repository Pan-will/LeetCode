"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
"""


class Solution(object):
    # 思路：首尾指针，前者存奇数，后者存偶数。直到二指针相遇。
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 判空
        if not nums:
            return []
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] % 2 == 1:
                i += 1
            elif nums[j] % 2 == 0:
                j -= 1
            elif nums[i] % 2 == 0 and nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.exchange([1, 3, 5]))
