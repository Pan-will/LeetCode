"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：
输入：name = "leelee", typed = "lleeelee"
输出：true

示例 4：
输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。
 

提示：
name.length <= 1000
typed.length <= 1000
name 和 typed 的字符都是小写字母。

思路：
i、j指针分别遍历name和typed：
若typed[j] == name[i]：i、j同步后移；
若typed[j] != name[i]：i不动、j后移；
j比i先遍历完，则返回false；否则返回true。
"""


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # 下标
        i = 0
        j = 0
        while i < len(name) - 1 and j < len(typed) - 1:
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                j += 1
        # i到末尾，j未到，返回true
        if i == len(name) - 1 and j < len(typed) - 1:
            return True
        # i、j都到末尾，且倒数第一个字符相同，返回true
        elif i == len(name) - 1 and j == len(typed) - 1 and name[-1:] == typed[-1:]:
            return True
        # 否则，返回false
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isLongPressedName("leelee","lleeelee"))
    print(solution.isLongPressedName("kikcxmvzi", "kiikcxxmmvvzz"))
