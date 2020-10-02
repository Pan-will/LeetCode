"""
给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

示例 1:

输入: J = "aA", S = "aAAbbbb"
输出: 3
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        for item in S:
            if item in J:
                ans += 1
        return ans

    def numJewelsInStones2(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        mydict = {}
        for item in J:
            if item in mydict.keys():
                mydict[item] += 1
            else:
                mydict[item] = 1
        ans = 0
        for item in S:
            if item in mydict.keys():
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numJewelsInStones(J="aA", S="aAAbbbb"))
