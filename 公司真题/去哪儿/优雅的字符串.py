"""
对于每个字符串都可以判断字符串的优雅程度。
她定义一个字符串 S[1..3n−2] (n≥2) 是一个半回文当且仅当它满足 S[i]=S[2n−i]=S[2n+i− 2] (1≤i≤n) .
例如dfgfdfg是一个半回文串，而dfgjfdfgj不是。
现在，Lisa 生成了一些长字符串。她请求你帮助找出有多少个半回文子串。
"""
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def solution(self, n, str):
        pass

    # 判断是否回文串
    def isHuiwen(self, s):
        if s == "":
            return True
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


n = int(input())
try:
    str = input()
except:
    str = None
s = Solution()
res = s.solution(n, str)
print(res)
