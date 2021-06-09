#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s):
        if not s:
            return True
        n = len(s)
        if n % 2 == 1:
            return False
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            else:
                temp = stack.pop()
                if ch == ")":
                    if temp != "(": return False
                elif ch == "]":
                    if temp != "[": return False
                else:
                    if temp != "{": return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("[["))
