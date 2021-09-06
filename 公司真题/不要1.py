def helper(n):
    while n > 0:
        if n % 10 != 1:
            return False
        n = n // 10
    return True


def isHaveOne(n):
    if n == 1: return True
    if n < 10: return False
    cur = n  # 保留原数字
    tar = []
    while cur > 0:
        t = cur % 10
        if t == 1: return True
        tar.append(t)
        cur = cur // 10
    print("n的构成：", tar)
    size = len(tar)  # n是几位数
    temp = []
    for i in range(2, size + 1):
        temp.append(int("1" * i))
    temp.sort(reverse=True)  # 降序排列
    print("预备因数：", temp)
    k = 0  # 遍历指针
    while n > 0 and k < len(temp):
        if helper(n): return True
        if n % temp[k] == 0: return True
        if n < temp[k]:  # 考虑n小于首个数的情况
            k += 1
            continue
        n = n % temp[k]  # 减到不能再减
        if n in temp: return True
        k += 1
    return False


while 1:
    s = input()
    if not s:
        break
    else:
        print(isHaveOne(int(s)))
