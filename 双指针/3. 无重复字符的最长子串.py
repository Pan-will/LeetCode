"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。


"""

# 思路：
# 单指针遍历字符串，每次判断当前字符是否已存在于res[]中，是则取res[]的长度length,不在则append。
# 每次取length要保留较大值，遍历完字符串时返回length。
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 原串长度为空，或仅有一个字符，返回原串长度
        if len(s) < 2:
            return len(s)
        res = []
        length = 0
        # 遍历原串
        for ch in s:
            # 若当前字符未出现在res中，则append，并更新当前非重复字符串长度
            if ch not in res:
                res.append(ch)
                length = max(length, len(res))
            # 若当前字符已出现在res中
            else:
                # 取length
                length = max(length, len(res))
                # 取当前字符已出现位置的下标
                index = res.index(ch)
                # 截取res,截掉当前字符
                res = res[index + 1:]
                # 将当前字符添加进res
                res.append(ch)
        return length


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("ay"))
