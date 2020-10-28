"""
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 你不需要考虑数组中超出新长度后面的元素。
"""


class Solution(object):
    # 思路：
    # 设两个指针cur、i，cur是有效元素下标，初值为0，i是从第一个元素开始的遍历指针；另外用count记录当前相同元素的个数；
    # i和cur指向的元素相同且count值小于2，说明cur指向的元素出现第二次，为有效元素，cur、i右移，count计数器加1；
    # i和cur指向的元素相同且count值不小于2，说明cur指向的元素出现已经大于两次，此后均是非有效元素，cur不动，仅i右移；
    # i和cur指向的元素不同，说明遇到新元素，为有效元素，cur、i右移，count计数器重置为1；
    # 返回值是有效元素个数，即cur+1
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        count = 1
        cur = 0
        i = 1
        while i < n:
            # i和cur指向的元素相同且count值小于2，说明cur指向的元素出现第二次，为有效元素，cur、i右移，count计数器加1；
            if nums[i] == nums[cur] and count < 2:
                cur += 1
                nums[cur] = nums[i]
                count += 1
                i += 1
            # i和cur指向的元素相同且count值不小于2，说明cur指向的元素出现已经大于两次
            elif nums[i] == nums[cur] and count >= 2:
                i += 1
            # i和cur指向的元素不同，说明遇到新元素，为有效元素
            elif nums[i] != nums[cur]:
                cur += 1
                nums[cur] = nums[i]
                count = 1
                i += 1
        return cur + 1

    # 上述方法简化
    # 因为元素是有序的，可以直接用nums[i]和nums[i-2]进行判断，如果相等，那么说明重复的元素一定超过了两个，当前元素需要跳过。
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for item in nums:
            if i < 2 or nums[i - 2] != item:
                nums[i] = item
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates2([0, 0, 1, 1, 1, 1, 2, 3, 3]))
