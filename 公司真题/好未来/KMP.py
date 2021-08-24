"""encoding=UTF-8"""
def kmp(self, S, T):
    lens = len(S)
    lent = len(T)
    # 判空
    if not S or not T or lens > lent:
        return 0
    ans = 0
    for i in range(lent - lens + 1):
        if T[i: lens + i] == S:
            ans += 1
            return ans


if __name__ == '__main__':
    pSrc = input()  # 主串
    pSub = input()  # 子串
    print(kmp(pSub, pSrc))