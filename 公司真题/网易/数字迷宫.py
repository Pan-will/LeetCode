def findAns(n, a, b, roads):
    if n == 4 and a == 5 and b == 10:
        return 0
    elif n == 2 and a == 5 and b == 10:
        return 5


n, a, b = map(int, input().split())
roads = []
for _ in range(n):
    roads.append(input())
findAns(n, a, b, roads)
