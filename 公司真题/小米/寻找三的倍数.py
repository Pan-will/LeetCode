class S(object):
    def getAns(self, arrs):
        if not arrs: return None
        i = 0
        while len(arrs) > 1:
            i = (i + 3) % len(arrs)
            arrs.pop(i-1)
            i -= 1
        return arrs[0]


if __name__ == '__main__':
    n = int(input())
    arrs = [i for i in range(1, n + 1)]
    s = S()
    print(s.getAns(arrs))
