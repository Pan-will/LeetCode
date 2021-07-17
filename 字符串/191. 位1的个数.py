class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = list(n)
        res = 0
        for ch in arr:
            if ch == "1":
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(0x00000000000000000000000000001011))
