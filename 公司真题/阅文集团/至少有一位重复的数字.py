"""
代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
@param N int整型
@return int整型

输入：20
输出：1
"""


class Solution:
    def numDupDigitsAtMostN(self, N):
        L = list(map(int, str(N + 1)))
        print("L =", L)
        res, n = 0, len(L)

        def help(m, n):
            return 1 if n == 0 else help(m, n - 1) * (m - n + 1)

        for i in range(1, n):
            res += 9 * help(9, i - 1)

        seen = set()
        for i, x in enumerate(L):
            tmp = sum(y not in seen for y in range(0 if i else 1, x))
            res += tmp * help(9 - i, n - i - 1)
            if x in seen:
                break
            seen.add(x)
        return N - res


if __name__ == '__main__':
    s = Solution()
    print(s.numDupDigitsAtMostN(20))
    # print(s.numDupDigitsAtMostN(100))
    # print(s.numDupDigitsAtMostN(10))
