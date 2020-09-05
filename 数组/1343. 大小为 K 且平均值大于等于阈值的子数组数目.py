"""
给你一个整数数组 arr 和两个整数 k 和 threshold 。
请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

示例 1：
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。
其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
"""


class Solution(object):
    # 法一：长度为k的滑动窗口，结果超时。
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        i = j = 0
        res = 0
        while j < k - 1:
            j += 1
        while j < len(arr):
            if sum(arr[i:j + 1]) / k >= threshold:
                res += 1
            i += 1
            j += 1
        return res

    # 法二：滑动窗口优化。
    def numOfSubarrays2(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        # 减少循环中的除法操作
        tar = k * threshold
        i = j = 0
        res = 0
        while j < k - 1:
            j += 1
        tempSum = sum(arr[i:j + 1])
        if tempSum >= tar:
            res += 1
        while j < len(arr) - 1:
            j += 1
            # 去尾加头，用加法来避免循环中的求和操作
            tempSum = tempSum - arr[i] + arr[j]
            i += 1
            if tempSum >= tar:
                res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numOfSubarrays2([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
