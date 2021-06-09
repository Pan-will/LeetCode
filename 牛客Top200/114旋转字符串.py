#
# 旋转字符串
# @param A string字符串
# @param B string字符串
# @return bool布尔型
#
class Solution:
    def solve(self, A, B):
        # write code here
        if len(A) != len(B): return False
        return B in A + A


if __name__ == '__main__':
    s = Solution()
    print(s.solve("youzan", "zanyou"))
