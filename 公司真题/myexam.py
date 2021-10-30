# 待完善



def help(nums):
    new_nums = []

    print(nums)
    temp_size = []
    i = 1
    while i < len(nums):
        ans = []
        if nums[i] - nums[i - 1] != 1:
            i += 1
            continue

        # 满足升序且连续
        while i < len(nums) and nums[i] - nums[i - 1] == 1:
            ans.append(nums[i - 1])
            i += 1
        if i >= len(nums):
            ans.append(nums[-1])
        print(ans)
        temp_size.append(len(ans))
    print(max(temp_size))


if __name__ == '__main__':
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums = [100, 4, 200, 1, 3, 2]

    help(nums)
