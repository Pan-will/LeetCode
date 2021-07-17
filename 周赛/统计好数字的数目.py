class Solution(object):
    def eliminateMaximum(self, n):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        return 5**((n+1)//2) * 4**(n//2)


if __name__ == '__main__':
    s = Solution()
    print(s.eliminateMaximum(1))
