"""
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，
并且这些子字符串中的所有0和所有1都是连在一起的——即0、1不能间隔排列。
相同的子串要分别计数。

示例 1 :
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（或者1）没有连在一起。

思路：
首先分析题目要求的子串特点：0和1数量必须相等且不能交叉排列，即子串一半是0、另一半是1。
1、遍历原串s，统计连续相同字符的个数，存到list中；
2、遍历list，每相邻两个元素，取其中较小者（相等则任取其一）添加到sum中；
3、返回sum。
"""


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 计数器
        num = 1
        # 初始化list
        listNum = [0] * len(s)
        # i是list的有效下标
        i = 0
        # 返回值
        sum = 0

        # 遍历原串s，从下标1开始
        for index in range(1, len(s)):
            # 当前字符与前一个相等，计数器加1
            if s[index] == s[index - 1]:
                num += 1
            # 当前字符与前一个不等，将上一个统计结果填到list中，list下标加1，重置计数器
            else:
                listNum[i] = num
                # print(listNum)
                i += 1
                num = 1
            # 填写最后一个统计结果
            if index == len(s) - 1:
                listNum[i] = num
                i += 1
        # print(listNum, i)
        # 遍历list，取相邻元素较小者，计算结果
        for j in range(1, i):
            sum += min(listNum[j - 1], listNum[j])
        return sum

    def countBinarySubstrings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        num1 = num0 = 0
        ans = 0
        for index, ch in enumerate(s):
            if index == 0:
                if ch == '0':
                    num0 += 1
                else:
                    num1 += 1
            else:
                if ch == '0':
                    num0 = num0 + 1 if s[index - 1] == '0' else 1
                    if num1 >= num0:
                        ans += 1
                elif ch == '1':
                    num1 = num1 + 1 if s[index - 1] == '1' else 1
                    if num0 >= num1:
                        ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    # print(solution.countBinarySubstrings("00110011"))
    print(solution.countBinarySubstrings("00110"))
