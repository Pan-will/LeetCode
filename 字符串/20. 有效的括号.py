"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
1、左括号必须用相同类型的右括号闭合。
2、左括号必须以正确的顺序闭合。
3、注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

思路：
栈；
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        # 用list来模拟栈
        listStr = list(s)
        listLeft = ['(', '[', '{']
        listRight = [')', ']', '}']
        result = []
        length = 0
        if listStr[0] in listRight or listStr[len(listStr) - 1] in listLeft:
            return False
        for num, ch in enumerate(listStr):
            if ch in listLeft:
                result.append(ch)
                length += 1
            elif ch in listRight:
                # 栈不为空才继续
                if length == 0:
                    return False
                # 取出反括号在集合中的下标
                i = listRight.index(ch)
                if len(result) != 0 and result[-1] != listLeft[i]:
                    return False
                else:
                    result.pop()
                    length -= 1

        if length != 0:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()[]{}"))
    print(solution.isValid("[])"))
    print(solution.isValid("()"))
    print(solution.isValid(""))
    print(solution.isValid("[["))
