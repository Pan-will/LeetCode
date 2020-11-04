"""
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution(object):
    # 注：sorted()可以排字符串
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mydict = {}
        for item in strs:
            temp = ''.join(sorted(item))
            if temp in mydict.keys():
                mydict[temp].append(item)
            else:
                mydict[temp]=[item]
        res = []
        for v in mydict.values():
            res.append(v)
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
