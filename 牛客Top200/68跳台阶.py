# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        a, b = 1, 2
        ans = a + b
        for i in range(3, number+1):
            ans = a + b
            a = b
            b = ans
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(5))
