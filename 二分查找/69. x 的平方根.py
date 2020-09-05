"""
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

思路：
用二分查找，端点值从0和x开始，当两端点数相邻了停止循环，返回左端点——较小者。
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        low, high = 0, x
        # 二分查找，当端点相邻了停止循环
        while high > low + 1:
            mid = int((high + low) / 2)
            if x / mid > mid:
                low = mid
            elif x / mid < mid:
                high = mid
            else:
                return mid
        return low


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(8))
