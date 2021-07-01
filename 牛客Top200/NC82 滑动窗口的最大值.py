# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size > len(num):
            return None
        cur = size - 1
        res = []
        while cur < len(num):
            res.append(max(num[cur-size+1:cur+1]))
            cur += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3))
