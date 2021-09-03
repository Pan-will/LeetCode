if __name__ == '__main__':
    # 控制台输入一个整数
    a = int(input())
    print(a)

    ##################
    ##################

    # 控制台输入两个整数，空格隔开
    m, n = map(int, input().split())
    print(m, n, "%.5f" % (m + n))

    ##################
    ##################

    # 控制台输入一个整数list
    arrs = list(map(float, input().split()))
    print(arrs)

    ##################
    ##################

    # 控制台循环输入，直到输入回车
    while 1:
        s = input()
        if not s:
            break
        else:
            a, b = s.split()
            print("%.3f" % (float(a) + float(b)))
