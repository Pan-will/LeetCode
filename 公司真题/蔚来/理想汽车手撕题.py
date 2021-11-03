# 题意：输入一个无序可重复整形数组，找到其中最大连续长度。
# 要求：不能首先利用排序，时间复杂度不大于O(n)。
def solve(nums):
    temp = [0 for _ in range(max(nums))]
    for num in nums:
        temp[num-1] = 1 if temp[num-1] == 0 else 1
    print(temp)
    res = 0
    ans = []
    for item in temp:
        if item != 0: res += 1
        else:
            ans.append(res)
            res = 0
    print("最大连续长度是：", max(ans))


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(len(nums), "输入的无序数组为：", nums)
    solve(nums)
"""
5 9 6 7 5 10 3 6 4 1 2
"""
