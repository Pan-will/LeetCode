class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 处理负数
        temp = True
        if x < 0:
            temp = False
            x = abs(x)
        # 处理被10整除的数
        while x > 0 and x % 10 == 0:
            x /= 10
            x = int(x)

        ans = 0
        while x > 0:
            tar = x % 10
            x = int(x / 10)
            ans = ans * 10 + tar

        if ans > 2147483647 or -ans < -2147483648:
            return 0

        if temp:
            return ans
        else:
            return -ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-1210))
    print(solution.reverse(120))
    print(solution.reverse(0))
    print(solution.reverse(1534236469))

