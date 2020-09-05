"""
给你一个字符串 s和整数k，从 s 中选择 k 个相邻且相等的字母删除它们，
使被删去的字符串的左侧和右侧连在一起。
你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
在执行完所有删除操作后，返回最终得到的字符串。
本题答案保证唯一。

示例 1：
输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。

示例 2：
输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"
"""


class Solution(object):
    # 递归
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in range(len(s) - k + 1):
            if s[i:i + k] == s[i] * k:
                return self.removeDuplicates(s[:i] + s[i + k:], k)
        return s

    # 将元素依次入栈并统计元素数量。每次入栈判断是否和栈顶元素相同：
    # 如果与栈顶元素相同，那么将栈顶元素的数量加1；
    # 如果栈顶元素数量达到3，则将栈顶元素出栈；
    # 如果待入栈元素与栈顶元素不同，那么直接入栈并将该元素个数置为1。
    # 遍历完字符串之后，将栈中剩余元素拼接即为答案。
    def removeDuplicates2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        ans = ""
        for ch, num in stack:
            ans += ch * num
        return ans


if __name__ == '__main__':
    solution = Solution()
    # print(solution.removeDuplicates2("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
    print(solution.removeDuplicates2(s="deeedbbcccbdaa", k=3))
