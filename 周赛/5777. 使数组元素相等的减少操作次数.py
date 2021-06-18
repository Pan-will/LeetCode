"""
输入：nums = [5,1,3]
输出：3
解释：需要 3 次操作使 nums 中的所有元素相等：
1. largest = 5 下标为 0 。nextLargest = 3 。将 nums[0] 减少到 3 。nums = [3,1,3] 。
2. largest = 3 下标为 0 。nextLargest = 1 。将 nums[0] 减少到 1 。nums = [1,1,3] 。
3. largest = 3 下标为 2 。nextLargest = 1 。将 nums[2] 减少到 1 。nums = [1,1,1] 。
"""


class Solution(object):
    def judgeEqu(self, arr):
        tem = set(arr)
        return True if len(tem) == 1 else False

    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or self.judgeEqu(nums):
            return 0
        if len(nums) == 2 and not self.judgeEqu(nums):
            return 1
        ans = 0
        # 降序排列
        nums.sort(reverse=True)
        while nums[0] != nums[-1]:
            i, j = 0, 1
            # 每一轮从头遍历,找到两个不同的数
            while nums[i] == nums[j]:
                i = j
                j += 1
            nums[i] = nums[j]
            ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reductionOperations([5, 1, 3]))
    print(s.reductionOperations([9, 7, 5, 3, 1]))
