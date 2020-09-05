"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
"""


class Solution(object):
    # 暴力，求得所有情况下的面积，取最大者返回
    # 时复O(n^2)、空复O(1)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                temp = min(height[i], height[j]) * (j - i)
                res = max(temp, res)
        return res

    # 双指针:
    # 难点是如何移动指针：为了寻找更大面积——所以i和j谁短移动谁。
    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i, j = 0, len(height) - 1
        while i < j:
            temp = min(height[i], height[j]) * (j - i)
            res = max(temp, res)
            # 移动指针，谁短移动谁
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
