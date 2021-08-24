def check(nums, m):
    nums.sort()
    for i in range(1, m + 1):
        if nums[i - 1] != i:
            return False
    return True


if __name__ == '__main__':
    n = input()
    n = int(n)
    res = []
    for _ in range(n):
        m = input()
        m = int(m)
        nums = input().split(" ")
        for i, digit in enumerate(nums):
            nums[i] = int(digit)
        if check(nums, m):
            res.append("Yes")
        else:
            res.append("No")
    for j in range(n):
        print(res[j])
