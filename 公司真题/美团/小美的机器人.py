if __name__ == '__main__':
    # 表示N个机器人
    n = input()
    n = int(n)
    left = []
    right = []
    origin = []

    for _ in range(n):
        temp = input().split(" ")  # 接收输入
        local = int(temp[0])  # 初始位置
        move = temp[1]  # 移动方向
        origin.append(local)
        if move == "R":
            right.append(local)
        elif move == "L":
            left.append(local)
    left.sort()
    right.sort()
    size = right[-1] if right[-1] > left[-1] else left[-1]
    res = [-999 for _ in range(size)]
    i, j = len(right) - 1, 0
    time = 0
    while left and right:
        if right[i] == left[j]:
            right.pop(i)
            left.pop(j)
            res[j - time] = time
        i += 1
        j -= 1
    if left:
        for j in left:
            res[j - time] = -1
    if right:
        for i in right:
            res[i - time] = -1
    ans = []
    for k in res:
        if k == -999: continue
        ans.append(k)
    for out in ans:
        print(out)
