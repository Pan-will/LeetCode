"""
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
返回可以通过分割得到的平衡字符串的最大数量。

示例 1：
输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
"""

"""
思路：
用栈，类似有效的括号。
从左到右遍历给定字符串，遇到R进栈，并用count计数，遇到一个L则count减1，当count=0时，说明找到一个新的子串。
重复上述过程，直到遍历结束。
"""


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        count = 0
        for ch in s:
            if ch == "R":
                count += 1
            else:
                count -= 1
            if count == 0:
                res += 1
        return res

    def balancedStringSplit2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        stackL = stackR = []
        numL = numR = 0
        for ch in s:
            if numL and numR and numL == numR:
                res += 1
                stackL = []
                stackR = []
                numL = 0
                numR = 0
            if ch == "L":
                numL += 1
                stackL.append(ch)
            else:
                numR += 1
                stackR.append(ch)
        return res + 1


if __name__ == '__main__':
    s = Solution()
    print(s.balancedStringSplit(s="LLLLRRRR"))
