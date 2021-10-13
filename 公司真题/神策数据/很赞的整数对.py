class Solution(object):
    def solve(self, x, y, m):
        # 特判已经满足的情况
        if x >= m or y >= m:
            return 0
        # 特判m=0，而x,y均为负数的情况
        if m == 0:
            if x < 0 and y < 0:
                return -1
        # 特判m>0，而x,y均为不大于0的情况
        elif m > 0:
            if x <= 0 and y <= 0:
                return -1
        res = 0
        temp = [x, y]
        while max(temp[0], temp[1]) < m:
            cur = sum(temp)
            max_v = max(temp[0], temp[1])
            if temp[0] > temp[1] and cur <= max_v:
                temp[1] = cur
            elif temp[0] > temp[1] and cur > max_v:
                temp[0] = cur
            elif temp[0] <= temp[1] and cur <= max_v:
                temp[0] = cur
            elif temp[0] <= temp[1] and cur > max_v:
                temp[1] = cur
            res += 1
        return res - 1


if __name__ == '__main__':
    s = Solution()
    x, y, m = map(int, input().split())
    print(s.solve(x, y, m))
