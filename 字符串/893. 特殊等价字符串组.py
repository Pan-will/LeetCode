"""
字符串数组 A，如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是特殊等价的。
一次移动包括选择两个索引 i 和 j，且 i ％ 2 == j ％ 2，交换 S[j] 和 S [i]。
现在规定，A 中的特殊等价字符串组是 A 的非空子集 S，
这样不在 S 中的任何字符串与 S 中的任何字符串都不是特殊等价的。
返回 A 中特殊等价字符串组的数量。
提示：
1 <= A.length <= 1000
1 <= A[i].length <= 20
所有 A[i] 都具有相同的长度。
所有 A[i] 都只由小写字母组成。

示例 1：
输入：["a","b","c","a","c","c"]
输出：3
解释：3 组 ["a","a"]，["b"]，["c","c","c"]

示例 2：
输入：["aa","bb","ab","ba"]
输出：4
"""


class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # set会自动去重
        res = set()
        # 遍历list
        for word in A:
            # 分别取出list各个元素的偶数位、奇数位字符，分别排序后拼接成字符串
            word = ''.join(sorted(word[::2]) + sorted(word[1::2]))
            # print(word)
            res.add(word)
        # 利用set的去重，即res中存在的都是互不等价的，返回res的长度即可
        return len(res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSpecialEquivGroups(["abcd", "adcb", "cbad", "cdab"]))
    print(solution.numSpecialEquivGroups(["aa", "bb", "ab", "ba"]))
    print(solution.numSpecialEquivGroups(["a", "b", "c", "a", "c", "c"]))
