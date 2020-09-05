"""
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。
注意，不是必须有这些素因子，而是必须不包含其他的素因子。
例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:
输入: k = 5
输出: 9

思路：3,5,7的排列组合
"""


class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        # 让1, 3, 5, 7先入列表, 加快4内读取速度, 所以3、5、7的值均为1
        num3 = num5 = num7 = 0
        numsList = [1]
        # if k <= 4:
        #     return numsList[k - 1]
        for _ in range(1, k):
            # 3, 5, 7取的数与对应3、5、7相乘, 所得三者间最小值
            addNum = min(numsList[num3] * 3, numsList[num5] * 5, numsList[num7] * 7)
            numsList.append(addNum)
            # 最小的数是3、5、7哪个相乘的, 对应数加1
            if addNum == numsList[num3] * 3:
                num3 += 1
            if addNum == numsList[num5] * 5:
                num5 += 1
            if addNum == numsList[num7] * 7:
                num7 += 1
        return numsList[k - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.getKthMagicNumber(k=5))
