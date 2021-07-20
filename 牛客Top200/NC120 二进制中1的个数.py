# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        if n < 0:
            n = n & 0xffffffff
        binNum = bin(n)[2:]
        arr = str(binNum)
        print(arr)
        res = 0
        for ch in arr:
            if int(ch) & 1 == 1:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(-2147483648))
    # print(s.NumberOf1(-1))
