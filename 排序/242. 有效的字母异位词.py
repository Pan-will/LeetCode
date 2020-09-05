"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

思路：
1、s和t长度不同，返回false；
2、转list，sort()，s==t则返回true，否则返回false。
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 长度不同，返回false
        if len(s) != len(t):
            return False
        # 转成list，按字母排序
        lists = list(s)
        lists.sort()
        listt = list(t)
        listt.sort()
        # 两串相同则返回true，否则返回false
        if lists == listt:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram(s="anagram", t="nagaram"))
