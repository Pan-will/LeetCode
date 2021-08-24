class Solution(object):
    def quickSort(self, arrs, low, high):
        if low >= high: return
        i, j = low, high
        base = arrs[low]
        while i < j:
            while i < j and arrs[j] > base:
                j -= 1
            arrs[i] = arrs[j]
            while i < j and arrs[i] < base:
                i += 1
            arrs[j] = arrs[i]
        arrs[i] = base
        self.quickSort(arrs, low, i - 1)
        self.quickSort(arrs, i + 1, high)

    def sub_sort(self, arr, low, high):
        cur = low - 1
        base = arr[high]  # 取最后一个元素为基准元素
        for i in range(low, high):
            # 当前元素小于或等于 pivot
            if arr[i] <= base:
                cur = cur + 1
                arr[cur], arr[j] = arr[j], arr[cur]
        arr[cur + 1], arr[high] = arr[high], arr[cur + 1]
        return cur + 1

    # 快速排序函数
    def quick_sort(self, arr, low, high):
        if low < high:
            base = self.sub_sort(arr, low, high)
            self.quick_sort(arr, low, base - 1)
            self.quick_sort(arr, base + 1, high)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums[-k]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
