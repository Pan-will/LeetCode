class Solution(object):
    # 法一：用list模拟，关键在于模拟循环的下标指针：index = (index + m -1) % n
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        nums = [i for i in range(n)]
        index = 0
        while n > 1:
            index = (index + m - 1) % n
            nums.pop(index)
            n -= 1
        return nums[0]

    def lastRemaining2(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == 1:
            return 0
        return (self.lastRemaining2(n - 1, m) + m) % n


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemaining2(5, 3))
