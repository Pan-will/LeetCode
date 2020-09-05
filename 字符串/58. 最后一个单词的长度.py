"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

示例:
输入: "Hello World"
输出: 5
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == " ":
            return 0
        tar = s.split()
        if len(tar):
            ans = tar[len(tar) - 1]
            return len(ans)
        else:
            return 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord("   "))
