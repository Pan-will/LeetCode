"""
给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。
如果数组中每个元素都不相同，则返回 false 。
 
示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

思路：
题意为：只要有一个元素出现次数>=2，则返回true；否则返回false；
利用list转set会去重的特点。
注：
len(setnums) == len(nums)时，说明每个元素都是唯一的，返回false；
只要去重后长度减小，说明有重复元素，则返回true。
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setnums = set(nums)
        # print(setnums)
        if len(setnums) == len(nums):
            return False
        else:
            return True

    """
    思路：排序后用遍历实现。
    """
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1, 5, 3, 4, 2]))
