"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        size = min(len(s), numRows)
        res = [[] for _ in range(size)]
        cur_row = 0
        go_down = 0
        for ch in s:
            res[cur_row].append(ch)
            # 只有当遍历到最上面一行或者最下面一行时，改变方向
            if cur_row == 0 or cur_row == numRows - 1:
                go_down = 1 if not go_down else 0
            cur_row += 1 if go_down else -1
        # print(res)
        ans = ""
        for item in res:
            ans += "".join(item)
        print(ans)

    def convert2(self, s, numRows):
        if not data:
            return ""
        size = len(data)
        if size <= numRows or numRows == 1:
            return data

        res = [[] for _ in range(numRows)]
        cur_row = 0
        # 表示放置字符的方向：向上或者向下
        down = 0
        for ch in s:
            res[cur_row].append(ch)
            if cur_row == 0 or cur_row == numRows - 1:
                down = 1 if not down else 0
            cur_row += 1 if down else -1
        print(res)
        ans = ""
        for item in res:
            ans += "".join(item)
        print(ans)


if __name__ == '__main__':
    s = Solution()
    # data = "abcdefghijklmno"
    data = "PAYPALISHIRING"
    s.convert(data, 3)
    s.convert2(data, 3)
