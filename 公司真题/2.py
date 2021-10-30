# 动态规划  01背包问题
def bag(n, c, w, v):
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    return value


if __name__ == '__main__':
    w = list(map(int, input().split()))
    v = list(map(int, input().split()))
    c = int(input())
    n = len(w)
    value = bag(n, c, w, v)
    print(value[n][c])

"""
2 1 2 2 3 5
3 5 2 3 1 4
10
"""
