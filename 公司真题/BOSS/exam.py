class S():
    def solve(self, a, b):
        i, j = 0, len(b) - 1
        while i < j:
            mid = i + (j - i) // 2
            if b[mid] == a[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return i
    def help(self,a,b):
        print(isinstance())


if __name__ == '__main__':
    s = S()
    print(s.solve("123456", "1233456"))
