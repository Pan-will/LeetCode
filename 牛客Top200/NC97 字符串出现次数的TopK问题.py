"""
输入：
["123","123","231","32"], 2

返回值：
[["123","2"],["231","1"]]

说明：
 "123"出现了2次，记["123","2"]，
 "231"与"32"各出现1次，但是"231"字典序在"32"前面，记["231","1"]，最后返回[["123","2"],["231","1"]]
"""


#
# return topK string
# @param strings string字符串一维数组 strings
# @param k int整型 the k
# @return string字符串二维数组
#
class Solution:
    def topKstrings(self, strings, k):
        if not strings:
            return None
        # 用字典统计每个单词的数量
        mydict = {}
        for word in strings:
            if word in mydict:
                mydict[word] += 1
            else:
                mydict[word] = 1
        # 按value域降序排列，返回值是list
        cur = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        mylist = []
        for item in cur:
            tar = []
            tar.append(item[0])
            tar.append(str(item[1]))
            mylist.append(tar)
        print("按value降序：", mylist)
        # 设置临时容器，存放相同value值的单词
        temp = [mylist[0]]
        i, j = 0, 1
        ans = []
        while j < len(mylist):
            # 若两个单词的频数相等
            if mylist[j][1] == mylist[i][1]:
                # value值相同则将单词放入temp中，准备字母排序
                temp.append(mylist[j])
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
                temp.append(mylist[i])
        # 最后一轮的temp还没有处理，别落下
        temp.sort()
        ans += temp
        return ans[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.topKstrings(["123","123","231","32"],2))
    print(s.topKstrings(["abcd", "abcd", "abcd", "pwb2", "abcd", "pwb2", "p12"], 3))
