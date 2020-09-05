"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

"""


class Solution(object):
    """
    思路：
    将原list中的数字拼接成字符串res；
    将int(res) + 1转成list。
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = ""
        for i in digits:
            res = res + str(i)
        res = str(int(res) + 1)
        return [int(i) for i in res]

    """
    思路：
    将原list中的数字取出，转成int类型res；
    将res + 1先字符串化，再转list[str]，再转list[int]。
    """
    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        res = 0
        for i, ch in enumerate(digits):
            res = res + ch * pow(10, i)
        digits = list(str(res+1))
        return [int(i) for i in digits]


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
