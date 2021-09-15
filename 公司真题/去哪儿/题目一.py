#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def solution(self, d):
        sum_d = sum(d)
        ex = sum_d % 3
        d.sort(reverse=True)  # 降序排列
        nums = [[], [], []]
        for num in d:
            nums[num % 3].append(num)
        if ex == 1:
            if nums[1]:
                nums[1].pop()
            elif len(nums[2]) >= 2:
                nums[2].pop()
                nums[2].pop()
            else:
                return ""
        elif ex == 2:
            if nums[2]:
                nums[2].pop()
            elif len(nums[1]) >= 2:
                nums[1].pop()
                nums[1].pop()
            else:
                return ""
        res = nums[0] + nums[1] + nums[2]
        res.sort(reverse=True)
        if not res:
            return ""
        if res[0] == 0:
            return "0"
        return "".join(str(ch) for ch in res)


_d_cnt = 0
_d_cnt = int(input())
_d_i = 0
_d = []
while _d_i < _d_cnt:
    _d_item = int(input())
    _d.append(_d_item)
    _d_i += 1
s = Solution()
res = s.solution(_d)
print(res + "\n")
