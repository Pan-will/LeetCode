# coding=utf-8
if __name__ == '__main__':
    res = []
    while 1:
        s = input()
        if s:
            a, b = s.split()
            res.append(round(float(a)+float(b), 4))
        else:
            break
    for item in res: print(item)

