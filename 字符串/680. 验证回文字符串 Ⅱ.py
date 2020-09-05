"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

示例 1:
输入: "aba"
输出: True

示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。

思路：
双指针：i从下标0往后、j从下标len(s)-1往前；
当不匹配时，将i或j向前移动一步，再进行匹配；
关键：不匹配时先移动哪个指针。
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 设置双指针
        i, j = 0, len(s) - 1
        # 设置标记——确保最多删除一个字符
        flag = True
        while i < j:
            if s[i] != s[j]:
                # 若遇到不回文，先判断标记：若为true说明之前没有遇到过不回文
                if not flag:
                    return False
                # 若i移动之后回文
                if s[i+1:j][::-1] == s[i+1:j]:
                    i += 1
                    # 调整过指针后要将标记置否
                    flag = False
                # 若j移动之后回文
                elif s[i:j-1][::-1] == s[i:j-1]:
                    j -= 1
                    # 调整过指针后要将标记置否
                    flag = False
                else:
                    return False
            # 回文则正常移动指针
            else:
                i += 1
                j -= 1
        return True

    def validPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 设置双指针
        i, j = 0, len(s) - 1
        # 设置标记——确保最多删除一个字符
        flag = True
        while i < j:
            if s[i] != s[j]:
                # 若遇到不回文，先判断标记：若为true说明之前没有遇到过不回文
                if not flag:
                    return False
                # 若i移动之后回文
                if Solution().isPalindrome(s, i + 1, j):
                    i += 1
                    # 调整过指针后要将标记置否
                    flag = False
                # 若j移动之后回文
                elif Solution().isPalindrome(s, i, j-1):
                    j -= 1
                    # 调整过指针后要将标记置否
                    flag = False
                else:
                    return False
            # 回文则正常移动指针
            else:
                i += 1
                j -= 1
        return True

    def isPalindrome(self, s, i, j):
        """
        :type s: str
        :type i: int
        :type j: int
        :rtype: bool
        """
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome2(self, s, i, j):
        """
        :type s: str
        :type i: int
        :type j: int
        :rtype: bool
        """
        if s[i:j][::-1] == s[i:j]:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
    # print(solution.validPalindrome("cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu"))
    print(solution.validPalindrome("eeccccbebaeeabebccceea"))
    print(solution.validPalindrome("abca"))
    print(solution.isPalindrome2("abcbc",2,5))
