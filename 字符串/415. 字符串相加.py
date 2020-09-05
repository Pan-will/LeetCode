"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return num1 if num2 == "0" else num2
        # 保证a串短，以a串为准进行遍历
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        # 反转
        num1 = num1[::-1]
        num2 = num2[::-1]
        # 两串长度统一
        while len(num1) < len(num2):
            num1 += "0"
        print("反转并统一长度后，两数分别为：", num1, num2)

        # 开始运算
        result = ""
        # 进位
        extra = 0
        for index, num in enumerate(num1):
            ans = (int(num) + int(num2[index]) + extra) % 10
            # 判断进位
            if int(num) + int(num2[index]) + extra >= 10:
                extra = 1
            else:
                extra = 0
            result += str(ans)
        # 只用判断最高位有进位，不用判断无进位情况
        if extra == 1:
            result += "1"
        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addStrings("123001", "456"))
    print(solution.addStrings("1", "9"))
