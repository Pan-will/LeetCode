"""
输入：startTime = "20:00", finishTime = "06:00"
输出：40
解释：你完成了从 20:00 到 00:00 的 16 个完整的对局，以及从 00:00 到 06:00 的 24 个完整的对局。
16 + 24 = 40

提示：
    startTime 和 finishTime 的格式为 HH:MM
    00 <= HH <= 23
    00 <= MM <= 59
    startTime 和 finishTime 不相等
"""


class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        begin = startTime.split(":")
        end = finishTime.split(":")
        # 转成int类型
        for i in range(2):
            begin[i] = int(begin[i])
            end[i] = int(end[i])
        # 通宵
        if (begin[0] > end[0]) or (begin[0] == end[0] and begin[1] > end[1]):
            t1 = (24 - begin[0] - 1) * 4 + (60 - begin[1]) // 15
            t2 = end[0] * 4 + end[1] // 15
            return t1 + t2
        # 没通宵
        else:
            hour = end[0] - begin[0]
            if hour == 0:
                if begin[1] > 0:
                    return ((end[1] // 15) * 15 - (1 + begin[1] // 15) * 15) // 15
                else:
                    return ((end[1] // 15) * 15 - (begin[1] // 15) * 15) // 15
            else:
                if begin[1] > end[1]:
                    return (hour - 1) * 4 + (60 - begin[1]) // 15 + end[1] // 15
                else:
                    if begin[1] > 0:
                        return hour * 4 + ((end[1] // 15) * 15 - (1 + begin[1] // 15) * 15) // 15
                    else:
                        return hour * 4 + ((end[1] // 15) * 15 - (begin[1] // 15) * 15) // 15


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfRounds("00:00", "23:59"))
