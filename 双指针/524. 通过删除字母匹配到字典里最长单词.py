"""
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:
输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
输出:
"apple"

示例 2:
输入:
s = "abpcplea", d = ["a","b","c"]
输出:
"a"
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        res = ""
        lists = list(s)
        for word in d:
            print("当前单词：", word)
            listword = list(word)
            # 设置双指针
            i, j = 0, 0
            while i < len(lists) and j < len(listword):
                # 若当前字符不同，则i后移，j不动
                if listword[j] == lists[i]:
                    j += 1
                i += 1
            if len(listword) == j and len(listword) > len(res):
                res = word
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLongestWord(s="abpcplea", d=["ale", "monkey", "apple", "plea"]))
