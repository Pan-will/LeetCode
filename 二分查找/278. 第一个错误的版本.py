"""
某产品的最新版本没有通过质量检测，每个版本都是基于之前的版本开发的，
所以错误的版本之后的所有版本都是错的。

假设有 n 个版本 [1, 2, ..., n]，想找出导致之后所有版本出错的第一个错误的版本。

已定义好的函数：bool isBadVersion(version) 可用来判断版本号 version 是否在单元测试中出错。
返回值true表示该版本出错，返回false表示该版本没有出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:
给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false，没出错
调用 isBadVersion(5) -> true，出错
调用 isBadVersion(4) -> true，出错
所以，4 是第一个错误的版本。 
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i < j:
            mid = i + int((j - i) / 2)
            if isBadVersion(mid):
                j = mid
            else:
                i = mid+1
        return j


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstBadVersion(5))
