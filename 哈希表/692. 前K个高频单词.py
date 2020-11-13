"""
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：
输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
"""


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # 用字典统计每个单词的数量
        mydict = {}
        for word in words:
            if word in mydict:
                mydict[word] += 1
            else:
                mydict[word] = 1
        # 按value域降序排列，返回值是list
        mylist = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        print(mylist)
        # 设置临时容器，存放相同value值的单词
        temp = [mylist[0][0]]
        i, j = 0, 1
        ans = []
        while j < len(mylist):
            if mylist[j][1] == mylist[i][1]:
                # value值相同则将单词放入temp中，准备字母排序
                temp.append(mylist[j][0])
                # 指针后移
                i += 1
                j += 1
            else:
                # 将相同value值的按字母排序，加到ans中
                temp.sort()
                ans += temp
                # temp清空，准备记录下一轮
                temp = []
                # 指针后移
                i += 1
                j += 1
                # 开始记录新的一轮
                temp.append(mylist[i][0])
        # 最后一轮的temp还没有处理，别落下
        temp.sort()
        ans += temp
        return ans[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
    print(s.topKFrequent(["love", "i", "leetcode", "i", "love", "coding"], k=2))
    print(s.topKFrequent(["aaa", "aa", "a"], 1))
