# coding=utf-8
import sys


class Solution(object):
    # 判断是否为回文串
    def isHuiwen(self, arrs):
        if len(arrs) < 2:
            return True
        i, j = 0, len(arrs) - 1
        while i < j:
            if arrs[i] != arrs[j]:
                return False
            i += 1
            j -= 1
        return True

    def getMinNum(self, string):
        temp = string[::-1]
        i = 0
        for i in range(len(string)):
            if temp[i:len(string)] == string[0:len(string) - i]:
                break
        return len(temp[0:i])

    def getMinNum2(self, string):
        n = len(string)
        base, mod = 131, 10 ** 9 + 7
        left = right = 0
        mul = 1
        best = -1
        for i in range(n):
            left = (left * base + ord(string[i])) % mod
            right = (right + mul * ord(string[i])) % mod
            if left == right:
                best = i
            mul = mul * base % mod
        add = ("" if best == n - 1 else string[best+1:])
        return len(add)


if __name__ == '__main__':
    res = []
    solu = Solution()
    for line in sys.stdin:
        if line == '\n': break
        s = line[:-1]
        if solu.isHuiwen(s):
            res.append(0)
        else:
            res.append(solu.getMinNum2(s))
    for ans in res:
        print(ans)
