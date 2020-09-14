"""
给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。

更正式地，检查是否存在两个下标 i 和 j 满足：

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

示例 1：

输入：arr = [10,2,5,3]
输出：true
解释：N = 10 是 M = 5 的两倍，即 10 = 2 * 5 。
"""


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if not arr:
            return True
        if arr.count(0) > 1:
            return True
        for item in arr:
            if item == 0:
                continue
            if 2 * item in arr:
                return True
        return False

    def checkIfExist2(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i, a in enumerate(arr):
            for j, b in enumerate(arr):
                if i != j and a == b:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkIfExist2([0]))
