"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。

示例 1：
输入：[2,1,2]
输出：5

示例 2：
输入：[1,2,1]
输出：0

示例 3：
输入：[3,2,3,4]
输出：10

示例 4：
输入：[3,6,2,3]
输出：8
 
提示：
3 <= A.length <= 10000
1 <= A[i] <= 10^6

思路：
想到：面积不为0，即能组成三角形，面积就不会是0，即满足两边之和大于第三边。
1、将数组A降序排列，三个指针：up,mid,low分别指向前三个元素；
    循环结束条件是：low=len(A)；
2、若满足两边之和大于第三边，即up<mid+low,则返回up+mid+low;
3、不满足up<mid+low，则三指针同步后移一位。
"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 在原址上降序排列
        A.sort(reverse=True)
        up, mid, low = 0, 1, 2
        while low < len(A):
            # 满足两边之和大于第三边，返回周长
            if A[up] < A[mid] + A[low]:
                return A[up] + A[mid] + A[low]
            # 否则三指针后移
            else:
                up, mid, low = mid, low, low + 1
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestPerimeter([3, 6, 2, 3]))
