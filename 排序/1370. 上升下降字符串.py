"""
给你一个字符串 s ，请你根据下面的算法重新构造字符串：

从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
重复步骤 2 ，直到你没法从 s 中选择字符。
从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
重复步骤 5 ，直到你没法从 s 中选择字符。
重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 结果字符串 。

 

示例 1：

输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
示例 2：

输入：s = "rat"
输出："art"
解释：单词 "rat" 在上述算法重排序以后变成 "art"

提示：
    1 <= s.length <= 500
    s 只包含小写英文字母。

思路：即先拼接string的升序序列，再拼接其降序序列。
1、将string转成list；
2、升序排list，各元素取一个拼接到res，将拼接过的元素从原list中删除；
3、降序排list，各元素取一个拼接到res，将拼接过的元素从原list中删除；
4、重复2和3，直到list为空。

若最小或者最大字符不止一个 ，只选其中任意一个拼接到结果字符串。
"""


class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 返回值
        res = ""
        # 转成list
        lists = list(s)
        # 直到原串为空，结束循环
        while len(lists) > 0:
            # 升序排列
            lists.sort(reverse=False)
            # 遍历前先清空
            temp = ""
            for i, ch in enumerate(lists):
                if ch not in temp:
                    temp += ch
            # 拼接结果
            res += temp
            # 将拼接过的字符从原list中删掉
            for i in range(len(temp)):
                lists.remove(temp[i])

            # 降序排列
            lists.sort(reverse=True)
            # 清空记录
            temp = ""
            for i, ch in enumerate(lists):
                if ch not in temp:
                    temp += ch
            # 拼接结果
            res += temp
            # 将拼接过的字符从原list中删掉
            for i in range(len(temp)):
                lists.remove(temp[i])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortString(s="bbbbccccaaaa"))
