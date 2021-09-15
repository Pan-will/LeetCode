def getAns(string):
    if not string: return None
    if len(string) == 1: return string
    cur = []
    size = 0
    res = []  # 记录答案字符
    # 遍历原串
    for i, ch in enumerate(string):
        if ch not in cur:
            cur.append(ch)
            size += 1
        else:
            # 备份当前为止，最长的无重复子串
            res = cur if len(res) < len(cur) else res
            # 若当前字符已存在，拿到下标
            tar_in = cur.index(ch)
            cur = cur[tar_in + 1:]
            cur.append(ch)
    return "".join(res)


if __name__ == '__main__':
    string = "abc2dac65428879654"
    print(getAns(string))
