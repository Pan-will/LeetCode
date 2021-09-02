while 1:
    try:
        t = int(input())
        for _ in range(t):
            a, b = map(int, input().split())
            print(a + b)
    except:
        break
