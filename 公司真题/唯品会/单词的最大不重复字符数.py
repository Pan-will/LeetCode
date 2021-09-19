#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param words string字符串一维数组 字符串数组
# @return int整型
#
class Solution:
    def maxSum(self, words):
        if not words or len(words) < 1:
            return 0
        if len(words) == 1:
            return len(words[0])
        # 返回值
        res = 0
        for i, word1 in enumerate(words):
            for j in range(i + 1, len(words)):
                if not self.hasSameWord(word1, words[j]):
                    continue
                else:
                    len1 = self.getDiffNum(word1)
                    len2 = self.getDiffNum(words[j])
                    res = max(res, len1 + len2)
        return res

    # 判断两个字符串是否有重复单词
    def hasSameWord(self, word1, word2):
        if not word2 or not word1:
            return True
        for ch in word1:
            if ch in word2:
                return False
        return True

    # 求一个字符串中不同字符的个数
    def getDiffNum(self, word):
        return len(set(list(word)))


if __name__ == '__main__':
    s = Solution()
    print(s.maxSum(["abcw", "baz", "foo", "bar", "fxyz", "abcdef"]))
    print(s.maxSum(["a", "aba", "abc", "d", "cd", "bcd", "abcd"]))
