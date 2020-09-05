"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，
所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 结果
        ans = []
        # 计数器
        num = 0
        stackNum = []
        # 重复字符串的最后一个字母的下标
        end = 0
        stackIndex = []
        for ch in s:
            # 判断数字
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch == "[":
                stackNum.append(num)
                num = 0
                stackIndex.append(end)
            if ch == "]":
                begin = stackIndex.pop()
                k = int(stackNum.pop())
                ans[begin:end] *= k
                end += (end - begin) * (k - 1)
            # 判断字母
            if ch.isalpha():
                ans.append(ch)
                end += 1
        return "".join(ans)


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString(s="3[a2[c]]"))
