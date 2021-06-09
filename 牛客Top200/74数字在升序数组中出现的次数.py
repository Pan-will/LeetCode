class Solution:
    def GetNumberOfK(self, data, k):
        left = self.getleft(data, k)
        right = self.getright(data, k)
        return right - left + 1

    def getleft(self, arr, tar):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if tar <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def getright(self, arr, tar):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if tar >= arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return right


if __name__ == '__main__':
    s = Solution()
    print(s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 3
                         ))
