"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution(object):
    # 思路：将单词拆分出来的字符作为dict的key即可
    # 注意：python中key不能是list，需要转成tuple类型。
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        mydict = {}
        for word in strs:
            chList = list(word)
            chList.sort()
            if tuple(chList) in mydict.keys():
                mydict[tuple(chList)].append(word)
            else:
                mydict[tuple(chList)] = [word]
        ans = []
        for value in mydict.values():
            ans.append(value)
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
