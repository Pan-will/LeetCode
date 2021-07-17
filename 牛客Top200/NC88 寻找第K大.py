# -*- coding:utf-8 -*-

class Solution:
    def findKth(self, a, n, K):
        print(a)
        self.quickSort(a, 0, n - 1)
        print(a)
        return a[K - 1]

    def quickSort(self, arr, begin, end):
        par = self.helper(arr, begin, end)
        if par >= begin + 1:
            self.quickSort(arr, begin, par - 1)
        if par < end - 1:
            self.quickSort(arr, par + 1, end)

    def helper(self, arr, l, r):
        temp = arr[l]  # 暂存基准值
        while l < r:
            while l < r and arr[r] <= temp:
                r -= 1
            if l >= r:
                break
            else:
                arr[l] = arr[r]
            while l < r and arr[l] >= temp:
                l += 1
            if l >= r:
                break
            else:
                arr[r] = arr[l]
        arr[l] = temp
        return l

    def quickSort2(self, arr, begin, end):
        if begin >= end:
            return
        i = begin
        j = end
        base = arr[begin]
        while i < j:
            while i < j and arr[j] < base:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] > base:
                i += 1
            arr[j] = arr[i]
        arr[i] = base
        self.quickSort(arr, begin, i - 1)
        self.quickSort(arr, i + 1, end)


if __name__ == '__main__':
    s = Solution()
    print(s.findKth([1, 3, 5, 2, 2], 5, 3))
