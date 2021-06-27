# -*- coding:utf-8 -*-
class Solution:
    # 思路：字典记录即可。
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        if len(s) < 2:
            return 0
        mydict = {}
        for ch in s:
            if ch in mydict.keys():
                mydict[ch] += 1
            else:
                mydict[ch] = 1
        for k, v in mydict.items():
            if v == 1:
                return s.index(k)
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.FirstNotRepeatingChar("google"))
