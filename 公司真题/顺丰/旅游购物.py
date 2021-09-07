def getAns(nums):
    up = []  # 放正数
    down = []  # 放负数
    for num in nums:
        if num >= 0:
            up.append(num)
        else:
            down.append(num)
    res = len(up)
    mval = sum(up)
    down.sort(reverse=True)
    for item in down:
        # print(mval+item)
        if mval + item >= 0:
            res += 1
            mval += item
    print(res)


n = int(input())
nums = list(map(int, input().split()))
getAns(nums)
"""
6
4 -4 1 -3 1 -3
"""
