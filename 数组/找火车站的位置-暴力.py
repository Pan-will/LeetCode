"""
字节跳动2020年9月第五批校招题。
输入m个居民居住点（坐标形式）、n个预备修建火车站的位置（坐标形式）；
找出一个合适的站点位置，使得所有居民到火车站的路径最短。
用例：
输入：
4 3
-1,-1
-1,1
1,-1
1,1
3,2
1,0
0,0
输出：
（1，0）
"""
import sys

class Solution():
    def findPosition(self, m, citizen, n, poi):
        minpoi = 1000000
        a, b = 0, 0
        # 遍历火车站预备位置
        for i in range(n):
            temp = 0
            # 遍历实名
            for j in range(m):
                temp += abs(poi[i][0] - citizen[j][0]) + abs(poi[i][1] - citizen[j][1])
            print(temp)
            if temp < minpoi:
                minpoi = temp
                a = poi[i][0]
                b = poi[i][1]
        return a, b


if __name__ == '__main__':
    # m是市民居住点的数量，n是预备火车站的数量
    # 先输入居民点，在输入预备站点。
    m, n = sys.stdin.readline().split()
    citizen = []
    poi = []
    for i in range(int(m)):
        data = sys.stdin.readline().rstrip().split('\t')
        x, y = data[0].split(',')
        citizen.append([int(x), int(y)])
    print("市民居住点是：", citizen)
    for i in range(int(n)):
        data = sys.stdin.readline().rstrip().split('\t')
        x, y = data[0].split(',')
        poi.append([int(x), int(y)])
    print("预备火车站点是：", poi)
    s = Solution()
    print(s.findPosition(int(m), citizen, int(n), poi))
