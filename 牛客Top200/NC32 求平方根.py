# @param x int整型
# @return int整型
#
class Solution:
    # 二分法
    def sqrt(self, x):
        if x < 2: return x
        i, j = 1, x // 2
        last = 0
        while i <= j:
            mid = i + (j - i) // 2
            if x // mid < mid:
                j = mid - 1
                last = mid
            elif x // mid > mid:
                i = mid + 1
                last = mid
            else:
                return mid
        return last

    # 直接返回平方根，向下取整
    def sqrt3(self, x):
        return int(x ** 0.5)

    # 奇数相加一定是平方数
    def sqrt2(self, x):
        res = 0
        begin = 1
        while x >= 0:
            x -= begin
            res += 1
            begin += 2
        return res - 1


if __name__ == '__main__':
    s = Solution()
    print(s.sqrt(0))
