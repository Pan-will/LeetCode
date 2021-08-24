"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [4,2,0,3,2,5]
输出：9
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        res = 0
        lmax = rmax = 0
        left, right = 0, len(height) - 1
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            if height[left] < height[right]:
                res += lmax - height[left]
                left += 1
            else:
                res += rmax - height[right]
                right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.trap(height=[4, 2, 0, 3, 2, 5]))
