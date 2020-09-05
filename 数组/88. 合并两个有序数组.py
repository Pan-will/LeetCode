"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]

思路：
指针i和j分别遍历nums1和nums2；
取两指针较小者追加到res中，较小指针后移，较大者不动；
若两指针相等，则两者都追加到res中，两指针均后移；
i<m或j<n时，停止遍历，将两串之一剩余的部分有序序列追加到res中。
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while j < n and i < m:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                i += 1
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                m += 1
            elif nums1[i] > nums2[j]:
                if i == 0:
                    nums1.insert(i, nums2[j])
                else:
                    nums1.insert(i - 1, nums2[j])
                j += 1
        if i == m and j < n:
            while j < n:
                nums1[i] = nums2[j]
                i += 1
                j += 1
        while nums1[-1] == 0:
            nums1.pop(-1)
        return nums1

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[0:m] + nums2
        nums1.sort()
        return nums1

    def merge3(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = -1, 0
        while j < len(nums2):
            nums1[i] = nums2[j]
            i -= 1
            j += 1
        nums1.sort()
        return nums1


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge3(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
    # print(solution.merge3(nums1=[2, 0], m=1, nums2=[1], n=1))
