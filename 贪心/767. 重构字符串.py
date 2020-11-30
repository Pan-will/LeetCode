"""
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:
输入: S = "aab"
输出: "aba"

示例 2:
输入: S = "aaab"
输出: ""
"""


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 特判
        if len(S) < 2:
            return S
        # 首先用字典统计各个字符的个数
        mydict = {}
        # 返回值
        res = ""
        for ch in S:
            if ch in mydict.keys():
                mydict[ch] += 1
            else:
                mydict[ch] = 1
        maxCh = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        if maxCh[0][1] > (len(S) + 1) // 2:
            return ""
        mylist = [[x[0], x[1]] for x in maxCh]
        while len(res) < len(S) and len(mylist) > 1:
            res = res + mylist[0][0] + mylist[1][0]
            mylist[0][1] -= 1
            mylist[1][1] -= 1
            # 每趟循环都要排序（模拟大顶堆），字符按频次降序
            mylist = sorted(mylist, key=lambda x: x[1], reverse=True)
            # 剔除频次为0的字符
            self.delZero(mylist)

        if mylist[0][1] != 0:
            res += mylist[0][0]
        return "".join(res)

    def delZero(self, mylist):
        if not mylist:
            return
        else:
            i = len(mylist) - 1
            while i > 0:
                if mylist[i][1] == 0:
                    mylist.pop(-1)
                    i -= 1
                else:
                    return


if __name__ == '__main__':
    s = Solution()
    print(s.reorganizeString("abbabbaaab"))
