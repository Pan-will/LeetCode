"""
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。
形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。

示例 1：
输入：[30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整数：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
"""


class Solution(object):
    # 遍历time[]，记录每个数%60的结果res[]，遍历res[]：若两数相加等于60，则满足要求。
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        needs = [0] * 60
        res = 0
        for i in time:
            if i % 60 == 0:
                res += needs[0]
            else:
                res += needs[60 - (i % 60)]
            needs[i % 60] += 1
        return res

    # 方法二：暴力搜索，超时。
    def numPairsDivisibleBy602(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
