"""
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。
返回出现次数最多，同时不在禁用列表中的单词。
题目保证至少有一个词不在禁用列表中，而且答案唯一。
段落中的单词不区分大小写。
禁用列表中的单词用小写字母表示，不含标点符号。
答案都是小写字母。

示例：
输入:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
输出: "ball"
解释:
"hit" 出现了3次，但它是一个禁用的单词。
"ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。
注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 "ball,"），
"hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
 

提示：

1 <= 段落长度 <= 1000
0 <= 禁用单词个数 <= 100
1 <= 禁用单词长度 <= 10
答案是唯一的, 且都是小写字母 (即使在 paragraph 里是大写的，即使是一些特定的名词，答案都是小写的。)
paragraph 只包含字母、空格和下列标点符号!?',;.
不存在没有连字符或者带有连字符的单词。
单词里只包含字母，不会出现省略号或者其他标点符号。

思路：
1、将整个段落中的字母转成小写；
2、用各标点符号分割段落；
3、遍历2返回的list，统计不在禁用表中且出现次数最多的单词并返回。
"""
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # 段落中的字母全部转成小写
        paragraph = paragraph.lower()
        # 用多种标点符号和空格分割段落
        listpara = re.split(r'[!?\'.;,\s]\s*', paragraph)
        print(listpara)
        # for index, word in enumerate(listpara):
        #     # 若有单词不是全由字母构成，则把该单词最后一位（标点符号）截掉
        #     if not word.isalnum():
        #         listpara[index] = word[0:-1]
        # 计数器
        num = 0
        # 返回值，即出现次数最多，同时不在禁用列表中的单词
        ans = ""
        for i, ch in enumerate(listpara):
            if ch not in banned and listpara.count(ch) > num:
                num = listpara.count(ch)
                ans = ch
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
    print(solution.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))

