"""
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。

示例 1：
输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
"""


class Solution(object):
    # 思路：
    # 从左往右遍历A，分别设置计数器记录上坡up和下坡down的长度；
    # 当不满足上坡了，就计数下坡；
    # 当下坡也不满足了，记录当前山脉的长度=up+down+1
    # 遍历时若遇到两个元素相等，则跳过。
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 遍历A的指针
        i = 1
        # 记录最长的山脉长度
        highMount = 0
        # 开始遍历
        while i < len(A):
            # 上下坡计数器，每次初值为0
            up = down = 0
            # 记录上坡长度
            while i < len(A) and A[i - 1] < A[i]:
                up += 1
                i += 1
            # 记录下坡长度
            while i < len(A) and A[i - 1] > A[i]:
                down += 1
                i += 1
            # 记录当前山脉长度
            if up > 0 and down > 0:
                highMount = max(highMount, up + down + 1)
            # 若遍历中碰到相同的元素，则跳过
            while i < len(A) and A[i] == A[i - 1]:
                i += 1
        return highMount


if __name__ == '__main__':
    s = Solution()
    print(s.longestMountain([2, 1, 4, 7, 3, 2, 5]))
