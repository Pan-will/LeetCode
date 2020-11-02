"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            nums1, nums2 = nums2, nums1
        l1 = len(nums1)
        res = []
        for item in nums1:
            if item in nums2 and item not in res:
                res.append(item)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
