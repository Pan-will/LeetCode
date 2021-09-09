import math


def answer(x: int) -> list[int]:
    # 调用第二步
    new_x = helper2(x)
    yue = []
    # 寻找所有约数，且默认升序排列
    for num in range(1, new_x + 1):
        if new_x % num == 0:
            yue.append(num)
    # yue += [new_x]
    # 若所有约数都严格大于10
    if yue[0] > 10:
        for i, n in enumerate(yue):
            yue[i] = n + 10
        return yue[:10]
    # 若所有约数小于等于10
    if yue[-1] <= 10:
        return yue


# 第一步实现
def helper1(x: int) -> int:
    return math.ceil(1539 / (x + 11))


# 第二步实现
def helper2(x: int) -> int:
    # 调用第一步
    tem = helper1(x)
    return 16 * tem


if __name__ == '__main__':
    ans = answer(5)
    print(ans)
