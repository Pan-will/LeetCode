def solve(n):
    sum = 0
    i = 1
    while i <= n - 1:
        if n % i == 0:
            sum += i
        i = i + 1
    print(sum == n)


if __name__ == '__main__':
    while 1:
        s = input()
        if not s:
            break
        else:
            solve(int(s))
