"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。

示例 1:
输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :
输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。

思路：
1、从左往右遍历，每一趟找出此前的最大值max,若nums[i]<max，则num[i]是需要参与重排的；
2、遍历到最右端，记录下最右边一个需要重排元素，其下标为high；
3、从右往左遍历，每一趟找出此前的最小值min,若nums[i]>min，则num[i]是需要参与重排的；
4、遍历到最左端，记录下最左边一个需要重排元素，其下标为low；
5、在nums中下标从low到high的元素即是需要重排的，返回值为：high-low+1。
注：若nums本就升序排列，则无需重排，返回值是0。
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 从左往右遍历，找high
        # big用来记录每一趟的最大值
        big = nums[0]
        high = 0
        for i in range(1, len(nums)):
            # 记录需要参与重排的元素的下标
            if nums[i] < big:
                high = i
            # 更换遍历中的最大值
            elif nums[i] > big:
                big = nums[i]
        # 从右往左遍历，找low
        # small用来记录每一趟遍历的最小值
        small = nums[-1]
        low = len(nums) - 1
        for j in range(len(nums) - 1, -1, -1):
            # 记录需要参与重排的元素的下标
            if nums[j] > small:
                low = j
            # 更变遍历中的最小值
            elif nums[j] < small:
                small = nums[j]
        # 若nums本就升序，无需重排
        if low - high + 1 == len(nums):
            return 0
        # 否则返回high - low + 1
        else:
            return high - low + 1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findUnsortedSubarray([1, 2, 3, 4]))
    print(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
