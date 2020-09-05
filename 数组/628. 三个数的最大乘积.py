"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
"""


class Solution(object):
    # 思路：就不要sort()【捂脸...】
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 处理nums中全是负数的情况
        ans = 1
        if max(nums) < 0:
            for i in range(3):
                ans *= max(nums)
                nums.remove(max(nums))
            return ans
        temp = []
        # 取两个绝对值最大的负数
        for i in range(2):
            if min(nums) < 0:
                temp.append(min(nums))
                nums.remove(min(nums))
        temp.append(max(nums))
        nums.remove(max(nums))
        j = 0
        while j < 2 and len(nums) != 0:
            temp.append(max(nums))
            nums.remove(max(nums))
            j += 1
        # 按绝对值大小降序排列
        temp.sort(key=abs, reverse=True)
        if len(temp) == 3:
            return temp[0] * temp[1] * temp[2]
        else:
            ans = temp[0] * temp[1]
            for i in range(2, len(temp)):
                if ans > 0 and temp[i] > 0:
                    return ans * temp[i]
                elif ans < 0 and temp[i] < 0:
                    return ans * temp[i]
        return ans

    def maximumProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 降序排列
        nums.sort(reverse=True)
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[1] * nums[-1], nums[0] * nums[-1] * nums[-2])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumProduct2([-1, -2, -3, -4, -5]))
