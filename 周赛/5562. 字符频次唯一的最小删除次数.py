"""
如果字符串 s 中 不存在 两个不同字符 频次 相同的情况，就称 s 是 优质字符串 。
给你一个字符串 s，返回使 s 成为 优质字符串 需要删除的 最小 字符数。
字符串中字符的 频次 是该字符在字符串中的出现次数。例如，在字符串 "aab" 中，'a' 的频次是 2，而 'b' 的频次是 1 。


示例 1：
输入：s = "aab"
输出：0
解释：s 已经是优质字符串。

示例 2：
输入：s = "aaabbbcc"
输出：2
解释：可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc" 。
"""


class Solution(object):
    # 1：用字典统计频次
    # 2：
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # step1:先用字典统计每个字符的频次
        mydict = {}
        for item in s:
            if item in mydict.keys():
                mydict[item] += 1
            else:
                mydict[item] = 1
        # 按values域升序,返回值是一个list
        list1 = sorted(mydict.items(),key=lambda x:x[1], reverse=False)
        list2 = [0 for _ in range(list1[-1][1] + 1)]
        # list2中的空位个数
        empty = len(list2) - len(list1)

        for item in list1:
            list2[item[1]] += 1

        # 统计需要优化的频次
        same = []
        for item in list2:
            if item > 1:
                same.append(item)
        print("same：",same)
        # 遍历values域，统计相同数字出现的次数



if __name__ == '__main__':
    s = Solution()
    print(s.minDeletions(s="aaabbbcc"))
