"""
给定一个由空格分割单词的句子 S。每个单词只包含大写或小写字母。
将句子转换为 山羊拉丁文，规则如下：

如果单词以元音开头（a, e, i, o, u），在单词后添加"ma"。
例如，单词"apple"变为"applema"。

如果单词以辅音字母开头（即非元音字母），移除第一个字符并将它放到末尾，之后再添加"ma"。
例如，单词"goat"变为"oatgma"。

根据单词在句子中的索引，在单词最后添加与索引相同数量的字母'a'，索引从1开始。
例如，在第一个单词后添加"a"，在第二个单词后添加"aa"，以此类推。
返回将 S 转换为山羊拉丁文后的句子。

示例 1:
输入: "I speak Goat Latin"
输出: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

思路：详见注释。
"""


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 定义元音字母集合
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # 用空格分割S
        words = S.split()
        # 返回值
        res = ""
        # 遍历S中的所有单词
        for i, word in enumerate(words):
            # 每个单词拼接时用空格隔开
            res += " "
            if word[0] in vowel:
                res = res + word + "ma" + 'a' * (i + 1)
            else:
                res = res + word[1:] + word[0] + "ma" + 'a' * (i + 1)
        # 截掉首位的空格
        return res[1:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.toGoatLatin("I speak Goat Latin"))
