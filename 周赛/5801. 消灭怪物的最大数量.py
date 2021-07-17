"""
输入：dist = [1,3,4], speed = [1,1,1]
输出：3
解释：
第 0 分钟开始时，怪物的距离是 [1,3,4]，你消灭了第一个怪物。
第 1 分钟开始时，怪物的距离是 [X,2,3]，你没有消灭任何怪物。
第 2 分钟开始时，怪物的距离是 [X,1,2]，你消灭了第二个怪物。
第 3 分钟开始时，怪物的距离是 [X,X,1]，你消灭了第三个怪物。
所有 3 个怪物都可以被消灭。
"""


class Solution(object):

    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not dist or not speed: return 0
        times = [(dist[i] - 1) // speed[i] for i in range(len(speed))]
        times.sort()
        for i in range(len(times)):
            if i > times[i]: return i
        return len(times)


if __name__ == '__main__':
    s = Solution()
    print(s.eliminateMaximum(dist=[4, 2, 3], speed=[2, 1, 1]))
    print(s.eliminateMaximum([1, 1, 2, 3], [1, 1, 1, 1]))
