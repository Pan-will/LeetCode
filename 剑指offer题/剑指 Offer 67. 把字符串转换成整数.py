class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        # 截掉开头的空格
        for i, ch in enumerate(str):
            if ch != " ":
                str = str[i:]
                break
        # 首字符是字母，则返回0
        if str[0].isalpha():
            return 0
        elif str[0] == "-":
            i = 1
            ans = 0
            while i < len(str) and ans < 2147483648:
                if str[i].isdigit():
                    ans = 10 * ans + int(str[i])
                    i += 1
                else:
                    break
            return -ans if ans < 2147483648 else -2147483648
        elif str[0] == "+":
            i = 1
            ans = 0
            while i < len(str) and ans < 2147483648:
                if str[i].isdigit():
                    ans = 10 * ans + int(str[i])
                    i += 1
                else:
                    break
            return ans if ans < 2147483648 else 2147483647
        else:
            i = 0
            ans = 0
            while i < len(str) and ans < 2147483648:
                if str[i].isdigit():
                    ans = 10 * ans + int(str[i])
                    i += 1
                else:
                    break
            return ans if ans < 2147483648 else 2147483647


if __name__ == '__main__':
    s = Solution()
    print(s.strToInt("  +1"))
    print(s.strToInt("   42"))
