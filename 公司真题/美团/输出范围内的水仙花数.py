import sys


class Solution(object):
    def isFlower(self, digit):
        if digit == 1: return True
        ori = digit
        digits = []
        while digit > 0:
            digits.append(digit % 10)
            digit = digit // 10
        back = 0
        for i in digits:
            back += i ** 3
        if back == ori:
            return True
        else:
            return False

    # 限制三位数的水仙花数
    def getFlower(self, low, high):
        if low > high: return ["no"]
        if high < 100: return ["no"]
        if low < 100: low = 100
        if high > 999: high = 999
        res = []
        for i in range(low, high + 1):
            if self.isFlower(i):
                res.append(i)
        if len(res) == 0: res.append("no")
        return res


if __name__ == '__main__':
    s = Solution()
    res = []
    for line in sys.stdin:
        if line == '\n': break
        m, n = line.split(" ")
        m = int(m)
        n = int(n)
        res.append(s.getFlower(m, n))
    print(res)
