#
# return the min number
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def minNumberdisappered(self, arr):
        # write code here
        if not arr:
            return 1
        arr.sort()
        while arr[0] <= 0:
            arr.pop(0)
        n = len(arr)
        for i in range(1, len(arr)):
            if arr[i - 1] != i:
                return i
        return n + 1


if __name__ == '__main__':
    s = Solution()
    print(s.minNumberdisappered([-1, -2, 1, 2, 3, 4]))
    print(s.minNumberdisappered([-1, 2, 3, 4]))
