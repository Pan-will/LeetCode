"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
注意：可以假定该字符串只包含小写字母。

案例:
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 初始化一个长为26的列表，用于统计原串中每个字符出现的个数
        index = [0] * 26
        # print(type(index), type(index[0]))
        for i in range(len(s)):
            index[ord(s[i])-ord("a")] += 1
        for j in range(len(s)):
            if index[ord(s[j])-ord("a")] == 1:
                return j
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstUniqChar("leetcode"))
    print(solution.firstUniqChar("loveleetcode"))