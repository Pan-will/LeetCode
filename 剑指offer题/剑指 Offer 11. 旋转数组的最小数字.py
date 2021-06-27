"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
"""


class Solution(object):
    # 思路：遍历，知道numbers[i] > numbers[i+1]时，numbers[i+1]即为所求。
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if len(numbers) < 2:
            return numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i - 1] > numbers[i]:
                return numbers[i]


if __name__ == '__main__':
    s = Solution()
    print(s.minArray([3, 4, 5, 1, 2]))
