"""
给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串；
如果不存在则返回 -1。
注意: A 与 B 字符串的长度在1和10000区间范围内。

示例 :
输入: A = "abcd"，B = "cdabcdab"。
输出: 3
解释：
A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；
A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
"""


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lenb = len(B)
        # 用来暂存原A串
        temp = A
        for i in range(1, int((lenb * 2) / (len(temp))) + 3):
            # 重复叠加A串
            A = temp * i
            # B串若是A的子串，则A串长度大于B串
            if len(A) < lenb:
                continue
            if B in A:
                return i
            # 遍历叠加后的A串
            # for index, ch in enumerate(A):
            #     # 满足B是A的子串，返回叠加次数，否则进入下一趟
            #     if ch == B[0] and A[index:index + lenb] == B:
            #         return i
            #     else:
            #         continue
            # continue
        return -1

    def repeatedStringMatch2(self, A, B):
        # 去两串的长度
        n1, n2 = len(A), len(B)
        t = int(n2 / n1) + 1
        ls = [t - 1, t, t + 1]
        for i in ls:
            if B in A * i:
                return i
        return -1

    def repeatedStringMatch3(self, A, B):
        n = int((len(B) * 2) / (len(A))) + 1
        for i in range(1, n + 2):
            if B in A * i:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedStringMatch("abcd", "cdabcdab"))
    print(solution.repeatedStringMatch("a", "aa"))
    print(solution.repeatedStringMatch("cccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccab","ccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabbcccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabccccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabacccbcabbcbbbbbcbacaaabbcbaaabaacbaabbbccaacbbbccabb"))
