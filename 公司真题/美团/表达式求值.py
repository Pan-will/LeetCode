def cul1(a, b):
    return a - (a & b)


def help(stack):
    if not stack:
        return 0
    n = len(stack)
    if n == 1: return int(stack[0])
    if n == 2: return cul1(int(cur[0]), int(cur[1]))
    while len(stack) > 1:
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(cul1(a, b))
    return stack[0]


s = input().split('@')
for i, item in enumerate(s):
    cur = [int(x) for x in item.split('#')]
    # print("当前第一优先级表达式：", cur)
    res = help(cur[::-1])
    s[i] = res
print(sum(s))

"""
1#4@3#6
123#12@13#133@23#12
"""
