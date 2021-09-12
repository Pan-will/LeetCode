def getAns(qujians):
    if not qujians:
        return 0
    res = 1
    # 将区间升序排列，先按区间左端点，左端点相同的按右端点排序
    qujians = sorted(qujians, key=lambda qujian: qujian[1])
    size = len(qujians)
    r = qujians[0][1]
    for i in range(1, size):
        if qujians[i][0] >= r:
            res += 1
            r = qujians[i][1]
    return size - res


def getAns2(qujians):
    if len(qujians) <= 1:
        return qujians
    res = []
    # 将区间升序排列，先按区间左端点，左端点相同的按右端点排序
    qujians = sorted(qujians, key=lambda qujian: (qujian[0], qujian[1]))
    for qujian in qujians:
        # 若res为空或者res中最后一个区间的右端点小于qujian区间的左端点，说明没有交集，可将qujian追加到res中
        if not res or res[-1][1] < qujian[0]:
            res.append(qujian)
        # 若res为空或者res中最后一个区间的右端点不小于qujian区间的左端点，说明有交集
        # res中最后一个区间的右端点替换为max(res中最后一个区间的右端点, qujian的右端点)
        elif res[-1][1] >= qujian[0]:
            res[-1][1] = max(res[-1][1], qujian[1])
    return res


origin = input()[2: -2].split(", ")
qujians = []
# print(len(origin), type(origin))
for item in origin:
    temp = [int(item[1]), int(item[3])]
    qujians.append(temp)
print(getAns(qujians))
