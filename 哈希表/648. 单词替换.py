"""
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。
例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。
如果继承词有许多可以形成它的词根，则用最短的词根替换它。
你需要输出替换之后的句子。

示例 1：
输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"

示例 2：
输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
"""


class Solution(object):
    # 思路：
    # 先把句子按空格分成单词；
    # 遍历每个单词中的字符，查看是否是词根，是则替换并遍历下一个单词。
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        listSen = sentence.split()
        for index, word in enumerate(listSen):
            temp = []
            for j in word:
                temp.append(j)
                if ''.join(temp) in dictionary:
                    listSen[index] = ''.join(temp)
                    break
        return ' '.join(listSen)


if __name__ == '__main__':
    s = Solution()
    print(s.replaceWords(dictionary=["a", "aa", "aaa", "aaaa"], sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
