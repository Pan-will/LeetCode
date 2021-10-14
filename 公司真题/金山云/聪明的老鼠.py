def findAns(migong, n):
    if not migong:
        return 0
    res = migong[0][0]
    pre_level_index = 0
    for level_index in range(1, n):
        max_num = max(migong[level_index])
        max_index = migong[level_index].index(max_num)
        if max_index == pre_level_index:
            pass


n = int(input())
migong = []
for _ in range(n):
    temp = list(map(int, input().split()))
    migong.append(temp)
findAns(migong, n)
