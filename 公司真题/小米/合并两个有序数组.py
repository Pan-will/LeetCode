class S(object):
    def getAns(self, arrs1, arrs2, m, n):
        i, j = 0, 0
        res = []
        while i < m and j < n:
            if arrs1[i] <= arrs2[j]:
                res.append(arrs1[i])
                i += 1
            else:
                res.append(arrs2[j])
                j += 1
        if i >= m and j < n:
            res += arrs2[j:]
        if i < m and j >= n:
            res += arrs1[i:]
        return res


if __name__ == '__main__':
    m_pre, n_pre = input().split(",")
    m, n = int(m_pre[-1]), int(n_pre[-1])
    arrs1 = list(map(int, input().split()))
    arrs2 = list(map(int, input().split()))
    s = S()
    print(s.getAns(arrs1, arrs2, m, n))
