"""
示例：

输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
输出：[true,false,false,true,true]
解释：
queries[0] : 子串 = "d"，回文。
queries[1] : 子串 = "bc"，不是回文。
queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。
queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。

"""


class Solution(object):
    # 判断字符串是否回文
    def isHuiwen(self, arrs):
        if len(arrs) < 2:
            return True
        i, j = 0, len(arrs) - 1
        while i < j:
            if arrs[i] != arrs[j]:
                return False
            i += 1
            j -= 1
        return True

    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        res = []
        if not s: return res
        for item in queries:
            temstr = s[item[0]: item[1]+1]
            print(temstr)
            res.append(self.isHuiwen(temstr))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.canMakePaliQueries(s="abcda", queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))
