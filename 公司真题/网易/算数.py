def findAns(n):
    res = bin(n).replace('0b', '')
    count = 0
    for ch in res:
        if ch == '1':
            count += 1
    return count


n = int(input())
print(findAns(n))
