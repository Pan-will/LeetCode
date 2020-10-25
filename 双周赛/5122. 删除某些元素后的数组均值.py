class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        sizearr = len(arr)
        delnum = int(sizearr * 0.05)
        res = arr[delnum:sizearr - delnum]
        # return round(sum(res) / len(res), 5)
        return sum(res) / len(res)


if __name__ == '__main__':
    s = Solution()
    print(s.trimMean(
        arr=[6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6,
             10, 8, 2, 3, 4]))
