class Solution():
    def judge(self, str):
        if not str: return "YES"
        stack = []
        for ch in str:
            if ch.isalpha():
                return "NO"
            elif ch == "(":
                stack.append(ch)
            else:
                if not stack:
                    return "NO"
                else:
                    stack.pop(-1)
        if not stack:
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    s = Solution()
    print(s.judge("()()()"))
