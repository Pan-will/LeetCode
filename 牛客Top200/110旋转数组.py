#
# 旋转数组
# @param n int整型 数组长度
# @param m int整型 右移距离
# @param a int整型一维数组 给定数组
# @return int整型一维数组
#
class Solution:
    def solve(self, n, m, a):
        pos = m % n
        return a[-pos:] + a[:-pos]


if __name__ == '__main__':
    s = Solution()
    print(s.solve(6, 7, [1, 2, 3, 4, 5, 6]))
