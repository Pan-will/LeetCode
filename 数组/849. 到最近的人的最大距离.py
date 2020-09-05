"""
在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
至少有一个空座位，且至少有一人坐在座位上。
你希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
返回他到离他最近的人的最大距离。

示例 1：
输入：[1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。

思路：
1、找到seats中第一、最后一个1的位置，分别为：low、high；
2、求得最后一个1的后面1的个数recindex（因为要坐最后那么所隔距离就为recindex）；
3、遍历seats从low到high的元素，用res[]存放每一段连续的0的个数；
4、求得res中的最大值leng，通过leng的奇偶求得最远距离ans；
5、返回max(low,recindex,ans)
注：要是seats中只有一个1，那么返回max(low,recindex),即首尾哪边离得远坐哪边。
"""


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # 记录最后一个1之后0的个数
        recindex = seats[::-1].index(1)
        # 分别找到第一个1和最后一个1的下标
        low = seats.index(1)
        high = len(seats) - 1 - recindex
        # seats中只有一个1，那就是首尾哪边离得远坐哪边
        if low == high:
            return max(low, recindex)
        # 存放seats中连续的0的个数
        res = []
        num = 0
        for i in range(low + 1, high + 1):
            if seats[i] == 0:
                num += 1
            else:
                res.append(num)
                num = 0
        # 取得最长连续0的个数，判断奇偶，因为坐就要坐中间
        leng = max(res)
        if leng % 2 == 1:
            ans = leng // 2 + 1
        else:
            ans = leng // 2
        # 返回是首、尾、及中间位置的最远距离
        return max(ans, low, recindex)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDistToClosest([1, 0, 0, 0]))
