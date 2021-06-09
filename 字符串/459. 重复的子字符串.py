"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:
输入: "abab"
输出: True     解释: 可由子字符串 "ab" 重复两次构成。

示例 2:
输入: "aba"
输出: False

思路：详见注释。
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 取字符串长度
        length = len(s)
        # 遍历，下标一定要从1，而不能从0开始
        for i in range(1, length):
            # 定义标记
            flag = 1
            # 若存在子串，那两者长度一定可以整除
            if length % i == 0:
                # 从整除点用新指针往后遍历，比较字符是否相等
                for j in range(i, length):
                    # 字符不同，即不满足子串条件
                    if s[j % i] != s[j]:
                        # 则当前的i不是周期, 标记置0，跳出循环
                        flag = 0
                        break
                # 若标记为真, 则i为最小周期
                if flag == 1:
                    return True
        # 未找到最小周期
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedSubstringPattern("aba"))
    print(solution.repeatedSubstringPattern("abab"))
    print(solution.repeatedSubstringPattern("abcabcabc"))
