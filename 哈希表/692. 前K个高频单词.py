"""
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：
输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
"""

import collections


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        mydict = {}
        for word in words:
            if word in mydict:
                mydict[word] += 1
            else:
                mydict[word] = 1
        mylist = sorted(mydict.items(), key=lambda x: x[1], reverse=True)[:k]
        temp = []
        ans = []
        for i in range(1, k):
            if mylist[i][1] == mylist[i - 1][1]:
                temp.append(mylist[i - 1][0])
            temp.sort()
            ans += temp

        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
    print(s.topKFrequent(["love", "i", "leetcode", "i", "love", "coding"], k=2))
