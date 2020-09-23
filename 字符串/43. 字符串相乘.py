"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        yinzi1 = 0
        for item1 in num1:
            yinzi1 = yinzi1 * 10 + int(item1)
        yinzi2 = 0
        for item2 in num2:
            yinzi2 = yinzi2 * 10 + int(item2)
        return str(yinzi1 * yinzi2)


if __name__ == '__main__':
    s = Solution()
    print(s.multiply("123", "456"))
