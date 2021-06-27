class Solution(object):
    # 二分法
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if target > nums[mid]:
                i = mid + 1
            else:
                j = mid
        if nums[i] != target:
            return 0
        else:
            # 此时i指向第一个target
            ans = 0
            while i < len(nums) and nums[i] == target:
                i += 1
                ans += 1
            return ans


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[1, 1, 2, 6, 9, 10], target=1))
    print(s.search([1], 1))
