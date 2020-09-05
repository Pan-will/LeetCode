"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

思路：双指针，就是反转字符串的思路，不过加了层非字母的判断。详见注释。
注：遇到非字母字符移动指针后不能忽略continue，因为不确定下一个字符就是字母。
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 转成list，字符串是不可变类型
        lists = list(S)
        # 双指针
        i, j = 0, len(lists) - 1
        while i < j:
            # 遇到非字母字符，仅移动指针
            if i < j and not lists[i].isalpha():
                i += 1
                continue
            if i < j and not lists[j].isalpha():
                j -= 1
                continue
            # 遇到字母，反转，再移动指针
            lists[i], lists[j] = lists[j], lists[i]
            i += 1
            j -= 1
        return "".join(lists)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))
