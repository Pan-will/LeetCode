"""
给定一个单词，判断单词的大写使用是否正确。定义在以下情况时，单词的大写用法是正确的：

1、全部字母都是大写，比如"USA"。
2、单词中所有字母都不是大写，比如"leetcode"。
3、如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。
注意: 输入是由大写和小写拉丁字母组成的非空单词。

示例 1:
输入: "USA"
输出: True

示例 2:
输入: "FlaG"
输出: False

思路：
Python提供了isupper()，islower()，istitle()方法用来判断字符串的大小写
"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper() or word.istitle():
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.detectCapitalUse("USA"))