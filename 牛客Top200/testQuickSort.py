class Solution:
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
        temp = arr[l]
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


if __name__ == '__main__':
    s = Solution()
    print(s.MySort(
        [884688278, 387052570, 77481420, 537616843, 659978110, 215386675, 604354651, 64838842, 830623614, 544526209,
         292446044, 570872277, 946770900, 411203381, 445747969, 480363996, 31693639, 303753633, 261627544, 884642435,
         978672815, 427529125, 111935818, 109686701, 714012242, 691252458, 230964510, 340316511, 917959651, 544069623,
         193715454, 631219735, 219297819, 151485185, 986263711, 805374069, 915272981, 493886311, 970466103, 819959858,
         733048764, 393354006, 631784130, 70309112, 513023688, 17092337, 698504118, 937296273, 54807658, 353487181,
         82447697, 177571868, 830140516, 536343860, 453463919, 998857732, 280992325, 13701823, 728999048, 764532283,
         693597252, 433183457, 157540946, 427514727, 768122842, 782703840, 965184299, 586696306, 256184773, 984427390,
         695760794, 738644784, 784607555, 433518449, 440403918, 281397572, 546931356, 995773975, 738026287, 861262547,
         119093579, 521612397, 306242389, 84356804, 42607214, 462370265, 294497342, 241316335, 158982405, 970050582,
         740856884, 784337461, 885254231, 633020080, 641532230, 421701576, 298738196, 918973856, 472147510, 169670404]))
