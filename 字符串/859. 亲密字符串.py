"""
给定两个由小写字母构成的字符串 A 和 B ，只要可以通过交换 A 中的两个字母得到与 B 相等的结果，
就返回 true ；否则返回 false 。
注意：A与B相等反而不合要求。
 

示例 1：
输入： A = "ab", B = "ba"
输出： true

示例 2：
输入： A = "ab", B = "ab"
输出： false

思路：
1、若A和B都为空，返回False；
2、若两串长度不同，返回False；
3、若A和B相等, 只要有重复元素，返回True；
4、若两串长度相同但不相等，统计不同字符的个数num，并记录其位置，若num>2，返回False；
5、将A中不同的两个字符交换位置，与B相等，返回True。
"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # A和B都为空，返回False
        if A == B == "":
            return False
        # 两串长度不同，返回False；
        if len(A) != len(B):
            return False
        # 若字符串相等, 只要有重复元素，返回True
        if A == B:
            for i, ch in enumerate(A):
                if A.count(ch) != 1:
                    return True
                else:
                    return False
        num = 0
        dif = [0] * len(A)
        for i, ch in enumerate(A):
            if ch != B[i]:
                dif[num] = i
                num += 1
        # 有两个以上的不同字符，不满足
        if num > 2:
            return False
        else:
            lista = list(A)
            lista[dif[0]], lista[dif[1]] = lista[dif[1]], lista[dif[0]]
            A = "".join(lista)
            if A == B:
                return True
            else:
                return False

    def buddyStrings2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B == "":
            return False
        # 两串长度不同，不满足
        if len(A) != len(B):
            return False
        num = 0
        dif = [0] * len(A)
        for i, ch in enumerate(A):
            if ch != B[i]:
                dif[num] = i
                num += 1
        # 有两个以上的不同字符，不满足
        if num > 2:
            return False

        # 不是由同一个字符组成的相同字符串，不满足
        if A == B and len(A) == 2 and A[::-1] != B:
            return False

        lista = list(A)
        lista[dif[0]], lista[dif[1]] = lista[dif[1]], lista[dif[0]]
        A = "".join(lista)
        if A == B:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.buddyStrings("abcd", "abcd"))  # False
    print(solution.buddyStrings("abcd", "badc"))  # False
    print(solution.buddyStrings("abab", "abab"))  # True
    print(solution.buddyStrings("", ""))
