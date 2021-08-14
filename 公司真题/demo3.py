if __name__ == "__main__":
    n, x, k = input().split(" ")
    n, x, k = int(n), int(x), int(k)
    res = [0 for _ in range(n)]
    res[x - 1] = 1
    for _ in range(k):
        i, j = input().split(" ")
        i, j = int(i), int(j)
        res[i - 1], res[j - 1] = res[j - 1], res[i - 1]
    for ans in range(n):
        if res[ans] == 1:
            print(ans + 1)
