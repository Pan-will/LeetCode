"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的
第一个位置 (从0开始)；
如果不存在，则返回  -1；
当 needle 是空字符串时：应返回 0 。

输入: haystack = "hello", needle = "ll"
输出: 2

输入: haystack = "aaaaa", needle = "bba"
输出: -1

"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 若子串为空
        if needle == "":
            return 0
        # 若两串相同
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        # 获取两个串的长度
        size1 = len(haystack)
        size2 = len(needle)
        print("两个串的长度分别是：", size1, size2)
        for index in range(size1):
            ans = index
            j = 0
            while j < size2 and ans < size1 and haystack[ans] == needle[j]:
                j += 1
                ans += 1
            if j == size2:
                return index
        return -1 if needle else 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("aaa", "a"))
    print(solution.strStr("hello", "lo"))
    print(solution.strStr("hello", "el"))
