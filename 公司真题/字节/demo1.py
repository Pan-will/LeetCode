class Solution:
    def ver(self, chars):
        res = []
        for char in chars:
            res.append(chr(96 + 123 - ord(char)))
        return "".join(res)

    def rev(self, chars):
        temp = self.ver(chars)
        print(temp, temp[::-1])
        return temp[::-1]

    def findKthBit(self, n, k):
        s = ["a"]
        if n < 2:
            return s[n - 1][k - 1]
        for i in range(1, n):
            s.append(s[i - 1] + chr(97 + i) + self.rev(s[i - 1]))
        print(s)
        return s[n - 1][k - 1]


if __name__ == '__main__':
    s = Solution()
    n, k = input().split(" ")
    n, k = int(n), int(k)
    print(s.findKthBit(n, k))
