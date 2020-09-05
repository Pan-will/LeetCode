"""
给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
如果数组不存在中心索引，那么我们应该返回 -1。
如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

示例 1:
输入:
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释:
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
"""


class Solution(object):
    # 运用数学技巧

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumi = 0
        s = sum(nums)
        for i in range(len(nums)):
            if 2 * sumi + nums[i] == s:
                return i
            sumi += nums[i]
        return -1

    # 双指针法
    """
    两个指针(左指针i，右指针j)都从左往右走，统计两边的和，和相等即返回;

    由于中心索引可以是所有有效下标：
        （1）左侧指针从-1开始，左侧累加和初始为零；
        （2）右侧指针从1开始，右侧累加和初始为：sum(nums) - nums[0]；

    循环条件：
    	右指针指向的下标小于数组长度，即：j < len(nums)；

    循环体：
        （1）若相等，则返回i+1
        （2）否则，左指针i右移，左侧和累加；右侧和减掉j指针当前指向的元素，再将右指针右移；

    另外，考虑到中心索引可能为len-1,所以循环体外需要再判断一次。
    """
    def pivotIndex2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return -1
        i, j = -1, 1
        sumi, sumj = 0, sum(nums) - nums[0]
        # print(sumi, sumj)
        while j < len(nums):
            if sumi == sumj:
                return i + 1
            else:
                i += 1
                sumi += nums[i]
                # 这里要注意：
                #   不能先j+=1，再计算sumj，因为当前j指向的值是sumj没有减掉的。
                sumj -= nums[j]
                j += 1
        if sumi == sumj:
            return i + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.pivotIndex2([-1, -1, -1, 0, -1, -1]))
