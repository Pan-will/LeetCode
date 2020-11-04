"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:
输入:
"tree"
输出:
"eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        mydict = {}
        for item in s:
            if item in mydict.keys():
                mydict[item] += 1
            else:
                mydict[item] = 1
        newlist = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        res = ""
        for i in newlist:
            res += "".join(i[0] * i[1])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort("tree"))
