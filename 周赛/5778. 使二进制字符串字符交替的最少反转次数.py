"""
给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次：

类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。
请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。

我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。

比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。
"""


class Solution(object):
    # 判断字符串是否交替
    def judge(self, s):
        if len(s) < 2:
            return True
        i, j = 0, 1
        while j < len(s):
            if s[i] == s[j]:
                return False
            else:
                i = j
            j = j + 1
        return True

    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        if self.judge(s):
            return 0
        ans = 0
        while not self.judge(s):

            ans += 1


if __name__ == '__main__':
    s = Solution()
    print(s.minFlips("1011101"))
