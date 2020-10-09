"""
将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。


示例：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return s[::-1]

    def reverseString2(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseString2(["h", "e", "l", "l", "o"]))
    print(solution.reverseString2(["h", "e", "l"]))
