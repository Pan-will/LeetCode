def findAns(n):
    if n == 1:
        return 1
    nums = []
    res = 0
    ori = n
    while n > 0:
        cur = n % 10
        if cur == 0:
            n = n // 10
            continue
        nums.append(cur)
        if ori % cur == 0:
            res += 1
        n = n // 10
    return res


n = int(input())
print(findAns(n))
