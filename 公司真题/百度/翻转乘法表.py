# 反转整数
def getRev_num(n):
    if n < 10:
        return n
    temp = []
    while n > 0:
        temp.append(n % 10)
        n = n // 10
    res = 0
    for num in temp:
        res = res * 10 + num
    return res


# 获取前n行反转后的乘法口诀表
def helper(n):
    if n < 1: return []
    res = []
    for i in range(1, n + 1):
        temp = []
        j = 1
        while j <= i:
            temp.append(getRev_num(j * i))
            j += 1
        res.append(temp)
    return res


def getAns(n, k):
    arr = helper(n)
    print(len(arr), arr)
    tar = arr[n - 1][:k]
    return max(tar)


def findAns(n, k):
    if n < 1 or k == 0: return 0
    temp = []
    j = 1
    while j <= n:
        temp.append(getRev_num(j * n))
        j += 1
    # print("第", n, "行为：", temp)
    tar = temp[:k]
    return max(tar)


n, k = map(int, input().split())
print(getAns(n, k))
print(findAns(n, k))
