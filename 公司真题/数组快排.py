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
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    s = Solution()
    print(alist)
    s.quick_sort(alist, 0, len(alist) - 1)
    print(alist)