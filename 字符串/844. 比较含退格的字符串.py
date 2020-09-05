"""
给定 S 和 T 两个字符串，判断二者是否相等，并返回结果。
# 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。

示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S == T:
            return True
        list1 = []
        list2 = []
        for i in range(len(S)):
            if S[i].isalpha():
                list1.append(S[i])
            else:
                if len(list1) == 0:
                    continue
                list1.pop()
        for j in range(len(T)):
            if T[j].isalpha():
                list2.append(T[j])
            else:
                if len(list2) == 0:
                    continue
                list2.pop()
        return "".join(list1) == "".join(list2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare(S="#ac", T="ad#c"))
