#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 将给定数组排序
# @param arr int整型一维数组 待排序的数组
# @return int整型一维数组
#
class Solution:
    # 快速排序
    def MySort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)
        return arr

    def quickSort(self, arr, begin, end):
        par = self.helper(arr, begin, end)
        if par >= begin + 1:
            self.quickSort(arr, begin, par - 1)
        if par < end - 1:
            self.quickSort(arr, par + 1, end)

    def helper(self, arr, l, r):
        temp = arr[l]  # 暂存基准值
        while l < r:
            while l < r and arr[r] >= temp:
                r -= 1
            if l >= r:
                break
            else:
                arr[l] = arr[r]
            while l < r and arr[l] <= temp:
                l += 1
            if l >= r:
                break
            else:
                arr[r] = arr[l]
        arr[l] = temp
        return l

    # 冒泡排序
    def BubbleSort_old(self, arr):
        if not arr or len(arr) < 2:
            return arr
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1, 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def BubbleSort_new(self, arr):
        if not arr or len(arr) < 2: return arr
        n = len(arr)
        flag = True
        while n - 1 > 0 and flag:
            flag = False
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    flag = True
            n -= 1
        return arr


if __name__ == '__main__':
    s = Solution()
    print(s.BubbleSort_new([5, 2, 3, 1, 4]))
