class Solution():
    def quick_sort(self, arr, low, high):
        if low >= high: return
        base = arr[low]
        i, j = low, high
        while i < j:
            while i < j and arr[j] > base:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] < base:
                i += 1
            arr[j] = arr[i]
        arr[i] = base
        self.quick_sort(arr, low, i-1)
        self.quick_sort(arr, i + 1, high)


if __name__ == '__main__':
    alist = [0, 1, 2, 1]
    s = Solution()
    print(alist)
    s.quick_sort(alist, 0, len(alist) - 1)
    print(alist)