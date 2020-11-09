"""
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
（这里，平面上两点之间的距离是欧几里德距离。）
你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

示例 1：
输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
"""


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]

    # 横纵坐标的平方和，放到新list中，然后将新list升序排，取前K个即可。
    def kClosest2(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        mydict = {}
        for item in points:
            temp = pow(item[0], 2) + pow(item[1], 2)
            if temp in mydict.keys():
                mydict[temp].append(item)
            else:
                mydict[temp] = [item]
        mylist = sorted(mydict.items(), key=lambda x: x[0])
        res = []
        num = 0
        for item in mylist:
            res += item[1]
            num += len(item[1])
            if num >= K:
                break
        return res[:K]


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
