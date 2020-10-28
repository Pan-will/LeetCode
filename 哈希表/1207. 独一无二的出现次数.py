"""
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

示例 1：
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。

示例 2：
输入：arr = [1,2]
输出：false
"""


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        mydict = {}
        for item in arr:
            if item in mydict.keys():
                mydict[item] += 1
            else:
                mydict[item] = 1
        vals = sorted(mydict.values())
        i, j = 0, 1
        while j < len(vals):
            if vals[i] == vals[j]:
                return False
            i += 1
            j += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.uniqueOccurrences([1, 2]))
