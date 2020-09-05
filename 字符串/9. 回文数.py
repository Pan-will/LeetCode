class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # 转成字符串
        string = str(x)
        i, j = 0, len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(-121))