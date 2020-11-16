"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。
每个 LED 代表一个 0 或 1，最低位在右侧。
给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

示例：
输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
"""


class Solution(object):
    # 反而思之：题目要根据num来匹配时间，既然给了范围，那就能用时间来照样匹配num！
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        # range函数左闭右开
        for i in range(0, 12):
            for j in range(0, 60):
                if (bin(i) + bin(j)).count("1") == num:
                    ans.append("%d:%02d" % (i, j))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.readBinaryWatch(2))
