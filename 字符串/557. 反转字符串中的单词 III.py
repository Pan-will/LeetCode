"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

示例 1:
输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 

思路：详见注释。
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 每个单词由空格分隔，所以先按空格截取字符串
        s = s.split()
        # print(type(s), type(s[0]))
        # 遍历集合，将其中的每个字符串元素反转
        for i in range(len(s)):
            s[i] = s[i][::-1]
        # 取集合中的元素并用空格拼接，然后返回拼接好的字符串
        return ' '.join(s)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("Let's take LeetCode contest"))
    print(solution.reverseWords("s'teL ekat edoCteeL tsetnoc"))