# 思路：将字母间的间隔求出，降序排列，丢弃前m个，剩下len(tar)-1-m个数求和即可。
# 注意：魔法键必须连续按下，不能只用来跳过远的步。
# 难点：保证在用魔法剑的范围内有最远的那一个间隔。
def findAns(tar, m):
    if len(tar) == 1:
        return 0
    if m >= len(tar)-1:
        return len(tar)
    # 存放每一步字母间的间隔
    dic = []
    for i in range(1, len(tar)):
        cur = ord(tar[i]) - ord(tar[i - 1])
        cur_r = cur if cur > 0 else -cur
        cur_l = 26 - cur_r
        dic.append(min(cur_r, cur_l))
    print("间距数组为：", dic)
    new_dic = sorted(dic, reverse=True)
    # 处理相同字符的情况
    if new_dic[0] == 0:
        return len(tar)
    # 找到原间隔数组中，最远的那一步
    big_i = dic.index(new_dic[0])

    return len(tar) + sum(new_dic[m:]) + m


tar, m = map(str, input().split())
m = int(m)
print(findAns(tar, m))
