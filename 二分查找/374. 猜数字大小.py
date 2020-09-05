"""
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
示例 :

输入: n = 10, pick = 6
输出: 6
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i < j:
            mid = i + int((j - i) / 2)
            if guess(mid) == -1:
                j = mid
            elif guess(mid) == 1:
                i = mid + 1
            elif guess(mid) == 0:
                return mid
        return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.guessNumber(10))
