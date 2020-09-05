"""
给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。

所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

说明:

给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:
输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

示例 2:
输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
"""


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        ans = []
        heaters.sort()
        for h in houses:
            l, r = 0, len(heaters) - 1
            while l < r:
                mid = int((l + r) / 2)
                if heaters[mid] < h:
                    l = mid + 1
                else:
                    r = mid
            # 若找到的值等于 house ，则说明 house 房屋处放有一个加热器，house 房屋到加热器的最短距离为 0
            if heaters[l] == h:
                ans.append(0)
            # 若该加热器的坐标值小于 house ，说明该加热器的坐标与 house 之间没有别的加热器
            elif heaters[l] < h:
                ans.append(h - heaters[l])
            # 若该加热器的坐标值大于 house 并且left不等于 0 ，说明 house 介于left和left-1之间，
            # 房屋到加热器的最短距离就是left和left - 1处加热器与 house 差值的最小值
            elif l:
                ans.append(min(heaters[l] - h, h - heaters[l - 1]))
            else:
                ans.append(heaters[l] - h)
        return max(ans)

    def findRadius2(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if len(heaters) == 1:
            return max(houses[-1] - heaters[0], heaters[0] - houses[0])
        i, j = 0, 1
        heaters.sort()
        while heaters[-1] > houses[-1]:
            heaters = heaters[0:-1]
        r = -1
        while j < len(heaters):
            r = max(r, (heaters[j] - heaters[i]) / 2)
            i = j
            j += 1
        r = max(houses[-1] - heaters[-1], r)
        return int(r)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRadius([1, 2, 3, 5, 15], [2, 30]))
