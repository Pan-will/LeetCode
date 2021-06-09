class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b


class Solution:
    # 思路其实很简单，每个区间按左端点升序排列；初始化返回值res=[];
    # 遍历所给的每个区间，要是res的右端点小于当前区间的左端点，则需合并；
    # 否则，当前区间并入res。
    def merge(self, intervals):
        # write code here
        if len(intervals) < 2:
            return intervals
        res = []
        # print(res[-1].start, res[-1].end)
        # 按区间的左端点升序排列
        intervals = sorted(intervals, key=lambda x: x.start)
        for interval in intervals:
            if not res:
                res.append(interval)
            elif res[-1].end < interval.start:
                res.append(interval)
            elif res[-1].end >= interval.start:
                res[-1].end = max(res[-1].end, interval.end)
        return res


if __name__ == '__main__':
    s = Solution()
    a = Interval(10, 30)
    b = Interval(20, 60)
    c = Interval(80, 100)
    d = Interval(150, 180)
    print(s.merge([a, b, c, d]))
