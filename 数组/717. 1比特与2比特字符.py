"""
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

示例 1:
输入:
bits = [1, 0, 0]
输出: True
解释:
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
"""


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) < 2:
            return True
        num = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == 1:
                num += 1
            else:
                break
        if num % 2 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isOneBitCharacter([1, 0, 0]))
