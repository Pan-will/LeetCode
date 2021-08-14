if __name__ == "__main__":
    n, k = input().split(" ")
    n, k = int(n), int(k)
    base = input().split(" ")
    dence = []
    for i in range(1, n):
        dence.append(int(base[i]) - int(base[i - 1]))
    tem = max(dence)
    if tem - k > 1:
        print(tem - k)
    else:
        print(1)
