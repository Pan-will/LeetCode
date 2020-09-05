"""
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：
    每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

示例 1：
输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
"""


class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTheLongestSubstring(s="eleetminicoworoep"))
