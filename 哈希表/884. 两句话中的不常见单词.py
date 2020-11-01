"""
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

返回所有不常用单词的列表。您可以按任何顺序返回列表。

示例 1：
输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]

示例 2：
输入：A = "apple apple", B = "banana"
输出：["banana"]
"""


class Solution(object):
    # 思路：自己出现一次，另一个没有出现，才算不常见。
    # 自己出现两次的，不论另一个中出不出现，都不算不常见。
    # 所以：为每一个句子创建一个dict，记录每个单词的出现次数。
    # 遍历A的字典，取出只出现一次的单词，拿到B的字典中比较。
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dicta = {}
        dictb = {}
        for i, item in enumerate(A.split()):
            if item in dicta.keys():
                dicta[item] += 1
            else:
                dicta[item] = 1
        for i, item in enumerate(B.split()):
            if item in dictb.keys():
                dictb[item] += 1
            else:
                dictb[item] = 1
        print("合并前的两个字典分别是：")
        print(dicta, dictb)
        for k, v in dictb.items():
            if k in dicta.keys():
                dicta[k] += v
            else:
                dicta[k] = v
        print("合并之后的字典：", dicta)
        res = []
        for k, v in dicta.items():
            if v == 1:
                res.append(k)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.uncommonFromSentences("abcd def abcd xyz", "ijk def ijk"))
