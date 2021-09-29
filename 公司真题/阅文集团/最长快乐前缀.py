#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return string字符串
#
class Solution:
    def longestPrefix(self, s: str) -> str:
        if not s:
            return ""
        size = len(s)
        if size < 2:
            return ""
        pre = []
        last = []
        cur = ""
        for i in range(size - 1):
            cur = cur + s[i]
            pre.append(cur)
        s = s[::-1]
        cur = ""
        for j in range(size - 1):
            cur = cur + s[j]
            last.append(cur[::-1])
        pre = pre[::-1]
        last = last[::-1]
        # print(pre, last)
        for a, b in zip(pre, last):
            if a == b:
                return a
        return ""


if __name__ == '__main__':
    s = Solution()
    print(s.longestPrefix("ababab"))
