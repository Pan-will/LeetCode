"""
给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。
最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。
输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。

说明:
空序列为所有字符串的子序列，任何字符串为其自身的子序列。
两个字符串长度均小于100。
字符串中的字符仅含有 'a'~'z'。

示例 :
输入: "aba", "cdc"
输出: 3
解析: 最长特殊序列可为 "aba" (或 "cdc")

思路：
若两串相同，返回-1；
若两串长度相同，内容不同，那二者本身均是各自的最长特殊序列；
若两串长度不同，长的那个串本身就是最长特殊序列；
"""


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLUSlength("aba", "cdc"))
    print(solution.findLUSlength("abc", "cdcd"))
