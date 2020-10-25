"""
给你一个字符串 text ，该字符串由若干被空格包围的单词组成。
每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。
题目测试用例保证 text 至少包含一个单词 。
请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。
如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。
返回 重新排列空格后的字符串 。

示例 1：
输入：text = "  this   is  a sentence "
输出："this   is   a   sentence"
解释：总共有 9 个空格和 4 个单词。可以将 9 个空格平均分配到相邻单词之间，相邻单词间空格数为：9 / (4-1) = 3 个。
"""


class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        # 统计字母个数、空格个数
        numSpace = 0
        numAlpha = 0
        for item in text:
            if item == ' ':
                numSpace += 1
            else:
                numAlpha += 1
        print(numAlpha, numSpace)
        words = text.split()
        # 若空格数能均分
        if numSpace % len(words) == 0:
            return
        # 否则，最大程度均分，多的放到返回值的最后


if __name__ == '__main__':
    s = Solution()
    text = "  this   is  a sentence "
    print(s.reorderSpaces(text))
