"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串：
    判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。
    如果可以构成，返回 true ；否则返回 false。
题目说明：杂志的上各个字母均只能用一次。

注：两个字符串均只含有小写字母。

示例：
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

思路：
0、magazine串的长度肯定要大些；
1、将两个字符串都转为list，方便删减元素；
2、用remove函数：默认删除原list中第一个匹配上的元素；
3、遍历ransom串，一旦magazine串中没有匹配的字符就退出遍历；
4、遍历指针未指向ransom串末尾，返回false；否则返回true。
"""


# 题目说明似乎是给题目注入了灵魂————一个字符只能用一次。
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 首先转成集合，方便遍历和删“杂志”中的元素
        list1 = list(ransomNote)
        list2 = list(magazine)
        if len(list2) < len(list1):
            return False
        i = 0
        while i < len(list1):
            if list1[i] in list2:
                list2.remove(list1[i])
                i += 1
            else:
                break
        if i != len(list1):
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct("aa", "ab"))
    print(solution.canConstruct("aa", "aab"))
