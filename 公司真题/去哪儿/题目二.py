"""
给定一个整数数组m，逐次选出任意整数，请返回所有对应整数、对应选出的次数的乘积之和能达到的最大值，可以放弃选择某些元素。
比如数组元素为[a1,a2,a3,a4]，依次选择a3，a2和a4，乘积之后的结果就是a3*1+a2*2+a4*3。
"""
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def solution(self, arr):
        if not arr:
            return 0
        # 现取数组长度，并升序排列
        size = len(arr)
        arr.sort()
        # 找到升序数组中的第一个正数
        cur_index = 0
        for i, num in enumerate(arr):
            if num > 0:
                cur_index = i
                break
        cur_index = cur_index if cur_index > 0 else 0
        # 记录最大值，即返回值，初始化为一个极小数
        res_max = -999999
        for j in range(cur_index, 0, -1):
            t = 1
            p = j
            tem = 0
            while tem <= size - j:
                tem += arr[p] * t
                t += 1
                p += 1
            res_max = max(res_max, tem)
        return res_max


_arr_cnt = 0
_arr_cnt = int(input())
_arr_i = 0
_arr = []
while _arr_i < _arr_cnt:
    _arr_item = int(input())
    _arr.append(_arr_item)
    _arr_i += 1

s = Solution()
res = s.solution(_arr)

print(str(res) + "\n")

"""
5
-1
1
4
-9
-8
"""