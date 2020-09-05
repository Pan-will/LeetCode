"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。

示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]

思路：
1、按字符串长度升序排列，以排序后的首字符串中的元素为目标；
2、遍历首字符串，每一趟遍历前要统计当前字符ch分别在首字符串和返回值ans中的个数：numi和numans；
3、若ch未在ans里出现过（即numans<1），且在剩余字符串中都出现过，则将ch追加到ans中；
    遍历剩余字符串时，若ch在当前字符串中未出现则结束本趟遍历，且不往ans中追加；
4、若ch在ans里出现过（即numans>1）：
    若ch在剩余字符串中的频数n（其中n = A[j].count(ch)）与在A[0]中的频数不同、
    并且ans中已经出现过n次，那当前字符不能往ans中追加；
"""


class Solution(object):
    # 理解有误
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        ans = []
        # 按字符串长度升序排列
        A.sort(key=lambda word: len(word))
        for i in A[0]:
            # 是否添加进ans的标志
            flag = True
            for j in range(1, len(A)):
                if i not in A[j]:
                    flag = False
                    break
            if flag:
                ans.append(i)
        return ans

    # 通过
    def commonChars2(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        ans = []
        # 按字符串长度升序排列
        A.sort(key=lambda word: len(word))
        for i in A[0]:
            # 统计当前字符在ans中的频数
            numans = ans.count(i)
            # 统计当前字符在A[0]中的频数
            numi = A[0].count(i)
            # 是否添加进ans的标志
            flag = True
            # 当前字符已经在ans中出现过
            if numans > 0:
                for j in range(1, len(A)):
                    # 若当前字符在后面的字符串中的频数n与在A[0]中的频数不同、
                    # 并且ans中已经出现过n次，那当前字符不能往ans中追加
                    if A[j].count(i) != numi and A[j].count(i) <= numans:
                        flag = False
                        break
            # 若当前字符在ans中没出现过
            else:
                for j in range(1, len(A)):
                    if i not in A[j]:
                        flag = False
                        break
            # 若标记为真，则可以追加进ans
            if flag:
                ans.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.commonChars2(
        ["bcaddcdd", "cbcdccdd", "ddccbdda", "dacbbdad", "dababdcb", "bccbdaad", "dbccbabd", "accdddda"]))
    print(solution.commonChars2(["bella","label","roller"]))
