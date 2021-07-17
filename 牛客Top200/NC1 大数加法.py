#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    # 思路：反转字符串，用i,j指针分别遍历两个串；
    # 结果放到其中一个串上（节约空间）；
    # 每一位相加都要维护进位extra；
    # 结果反转并返回

    def solve(self, s, t):
        if not s and not t: return None
        if not s and t: return t
        if s and not t: return s
        s = s[::-1]
        t = t[::-1]
        n = len(s) if len(s) <= len(t) else len(t)
        res = []
        extra = 0  # 表示进位
        i = 0
        while i < n:
            tem = int(s[i]) + int(t[i]) + extra
            extra = tem // 10
            res.append(tem % 10)
            i += 1
        if len(s) > len(t):
            while i < len(s):
                tem = int(s[i]) + extra
                extra = tem // 10
                res.append(tem % 10)
                i += 1
        else:
            while i < len(t):
                tem = int(t[i]) + extra
                extra = tem // 10
                res.append(tem % 10)
                i += 1
        if extra > 0:
            res.append(extra)
        return self.processRes(res[::-1])

    def processRes(self, arr):
        if len(arr) == 0: return 0
        res = 0
        for item in arr:
            res = 10 * res + item
        return str(res)


if __name__ == '__main__':
    s = Solution()
    print(s.solve("733064366", "459309139"))
