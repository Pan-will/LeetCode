"""
思路：
首先建立一个map来映射符号和值，然后遍历字符串：
若当前字符代表的值不小于其右边，就加上该值；否则就减去该值。
以此类推到最左边的数，最终得到的结果即是答案。
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        myMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        length = len(s)
        for i in range(length):
            # 注意比较的是map里的value(加上myMap[])，而不是index
            if i < length-1 and myMap[s[i]] < myMap[s[i+1]]:
                result -= myMap[s[i]]
            else:
                result += myMap[s[i]]
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("III"))
