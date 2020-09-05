"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

思路：用栈。
1、intervals中各区间左端点取出，放入left{}，转set时会自动去重、升序排列；
2、各区间右端点取出，放入right{}；
3、构造pos = list[[] for i in range(len(left) + len(right))];
4、用指针i遍历left，pos[i].append(1)；
5、用指针j遍历right，pos[j].append(-1)；
6、遍历pos，用start记录pos[index]!=[]的起始位置，令sum+=pos[index],若sum=0时追加[start,index]到res中。
7、返回res。
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        left = []
        right = []
        for ch in intervals:
            left.append(ch[0])
            right.append(ch[1])
        # 转set，自动去重、升序排列
        setl = set(left)
        setr = set(right)
        # print(setl, setr)
        pos = [[]for i in range(len(setl) + len(setr))]
        # print(pos, len(pos), len(setl), len(setr))

        # 用指针i遍历left，pos[i].append(1)
        for i in range(len(setl)):
            pos[i].append(1)
        # 用指针j遍历right，pos[j].append(-1)；
        for j in range(len(setr)):
            pos[j].append(-1)
        print(pos)
        flag = 0
        # 遍历pos，用start记录pos[index]!=[]的起始位置，令sum+=pos[index],若sum=0时追加[start,index]到res中。
        for index in range(len(pos)):
            if len(pos[index]) != 0:
                start = index

            if 1 in pos[index]:
                flag += 1
            elif -1 in pos[index]:
                flag -= 1
            if flag == 0:
                res.append([start, index])
                start = index
        return res

    def merge2(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        res = []
        # 将区间升序排列，先按区间左端点，左端点相同的按右端点排序
        intervals = sorted(intervals, key=lambda interval: (interval[0], intervals[1]))
        # 遍历intervals，interval为当前区间
        for interval in intervals:
            # 若res为空或者res中最后一个区间的右端点小于interval区间的左端点，说明没有交集，可将interval追加到res中
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # 若res为空或者res中最后一个区间的右端点不小于interval区间的左端点，说明有交集
            # res中最后一个区间的右端点替换为max(res中最后一个区间的右端点, interval的右端点)
            elif res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[2, 2], [2, 5], [4, 5], [6, 7], [8, 9], [1, 10]]))
    # print(solution.merge([[1, 4], [0, 4]]))
