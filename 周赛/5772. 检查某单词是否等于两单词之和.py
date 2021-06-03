class Solution(object):
    def getNum(self, word):
        res = 0
        for i in word:
            res = res * 10 + (ord(i) - ord("a"))
        return res

    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        f = self.getNum(firstWord)
        s = self.getNum(secondWord)
        c = self.getNum(targetWord)
        return f + s == c


if __name__ == '__main__':
    s = Solution()
    print(s.isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb"))
