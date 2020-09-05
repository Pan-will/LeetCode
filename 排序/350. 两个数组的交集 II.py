"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 保证s1短
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # 返回值
        res = [int] * len(nums1)
        # res下标
        index = 0

        # 遍历s1
        i = 0
        while i < len(nums1):
            # 数字在s2中，不在res中，则添加到res中，下标加1，指针后移
            if nums1[i] in nums2 and nums1[i] not in res:
                # 该数字分别在两个list中出现的次数，取较小者
                num = min(nums1.count(nums1[i]), nums2.count(nums1[i]))
                # 在res中重复加入num个该数字
                for j in range(num):
                    res[index] = nums1[i]
                    index += 1
                i += 1
            # 指针后移
            else:
                i += 1
        return res[0:index]

if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
    print(solution.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))