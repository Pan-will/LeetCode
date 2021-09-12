def getAns(row, column, jianpan, move, zhuan, kit, tar):
    res = 0
    # 机械手初始位置
    begin_i = 0
    begin_j = 0
    for ch in tar:
        for i, cur_row in enumerate(jianpan):
            if ch in cur_row:
                ch_index = cur_row.index(ch)
                res = res + (i-begin_i) + (ch_index-begin_j)
    return res


n, m, x, y, z = map(int, input().split())
jianpan = []
for _ in range(n):
    temp = list(input())
    jianpan.append(temp)
tar = list(input())
# print(jianpan)
# print(tar)
print(getAns(n, m, jianpan, x, y, z, tar))
