# coding=utf-8
import sys
if __name__ == '__main__':
    res = []
    while 1:
        s = raw_input()
        if s != "":
            a, b = s.split()
            res.append(round(int(a)+int(b), 3))
        else:
            break
    print res

