"""
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:
 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]

示例2:
 输入：S = "ab"
 输出：["ab", "ba"]

提示:
字符都是英文字母。
字符串长度在[1, 9]之间。
"""


class Solution(object):
    # 要得到3个a、2个c和1个b的全排列，你首先需要选择一个起始字符：a、b或c。如果是a，那么你需要2个a、2个c和1个b的全排列。
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        mydict = {}
        for ch in S:
            if ch in mydict.keys():
                mydict[ch] += 1
            else:
                mydict[ch] = 1
        print(mydict, len(mydict))


if __name__ == '__main__':
    s = Solution()
    print(s.permutation("aab"))
