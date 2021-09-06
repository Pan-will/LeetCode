def search(nums, target):
    if target > nums[-1]:
        return len(nums) - 1
    i, j = 0, len(nums) - 1
    while i < j:
        mid = i + (j - i) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    return i


if __name__ == '__main__':
    nums = [1, 2, 3, 5, 6, 7]
    print(search(nums, 7))
