"""
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4 or 12 < n:
            return []
        res = []
        path = []

        self.backtrace(s, 0, n, res, path)
        return res

    def backtrace(self, s, begin, n, res, path):
        # 路径长度为4，且刚好把字符串遍历完，说明找到了一个答案
        if len(path) == 4:
            if begin == n:
                res.append('.'.join(path))
            return

        if begin == n:
            return

        if s[begin] == '0':
            path.append('0')
            self.backtrace(s, begin + 1, n, res, path)
            path.pop()  # 回退
        else:
            for i in range(begin, n):
                cur_num = int(s[begin: i + 1])
                if 0 <= cur_num <= 255:
                    path.append(str(cur_num))
                    self.backtrace(s, i + 1, n, res, path)
                    path.pop()  # 回退
                else:
                    break

    def restoreIpAddresses2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4 or n > 12:
            return []
        temp = []
        res = []
        self.dfs(s, 0, n, temp, res)
        return res

    def dfs(self, s, begin, n, temp, res):
        # 若临时list中元素正好4个，且刚好把给定字符串遍历完，说明找到一个答案
        if len(temp) == 4:
            if begin == n:
                res.append(".".join(temp))
            return
        if begin == n:
            return
        # 遍历途中遇到0字符
        if s[begin] == '0':
            temp.append('0')
            self.dfs(s, begin + 1, n, temp, res)
            temp.pop()
        else:
            for i in range(begin, n):
                num = int(s[begin: i + 1])
                # if num >= 0 and num <= 255:
                if 0 <= num <= 255:
                    temp.append(str(num))
                    self.dfs(s, begin + 1, n, temp, res)
                    temp.pop()
                else:
                    break


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses2("25525511135"))
