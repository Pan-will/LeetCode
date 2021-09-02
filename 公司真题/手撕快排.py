# coding=utf-8
class Solution():
    def sub_sort(self, arr, low, high):
        i = low - 1
        base = arr[high]  # 取最后一个元素为基准元素
        for j in range(low, high):
            # 当前元素小于或等于 pivot
            if arr[j] <= base:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # 快速排序函数
    def quick_sort(self, arr, low, high):
        if low < high:
            base = self.sub_sort(arr, low, high)
            self.quick_sort(arr, low, base - 1)
            self.quick_sort(arr, base + 1, high)

    def quickSort(self, arr, low, high):
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
        self.quickSort(arr, low, i - 1)
        self.quickSort(arr, i + 1, high)


if __name__ == '__main__':
    s = Solution()
    # array = [6, 2, 5, 1, 4, 3]
    # array = [0, 1, 2, 1]
    # array = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    array = [5,1,1,2,0,0]
    print(array)
    s.quick_sort(array, 0, len(array) - 1)
    # s.quickSort(array, 0, len(array) - 1)
    print(array)
