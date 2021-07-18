"""
操作数都是个位数，如3+2
且仅支持加减法。
"""
class Solution:
    def opera(self, b, op, a):
        if op == "+":
            return b + a
        elif op == "-":
            return b - a
        else:
            return b * a

    # 以括号为准，遇到左括号进栈，遇到右括号，出栈直到左括号；
    # 将计算的值入栈。直到遍历字符串完成。
    def solve(self, s):
        # 判空
        if not s:
            return 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == "+" or ch == "-" or ch == "*":
                stack.append(ch)
            elif ch.isdigit():
                stack.append(int(ch))
            elif ch == ")":
                a = stack.pop(-1)
                op = stack.pop(-1)
                b = stack.pop(-1)
                stack.pop(-1)  # 将多余的左括号出栈
                tem = self.opera(b, op, a)
                stack.append(tem)
        if len(stack) > 1:
            a = stack.pop(-1)
            op = stack.pop(-1)
            b = stack.pop(-1)
            return self.opera(b, op, a)
        else:
            return stack[0]


if __name__ == '__main__':
    s = Solution()
    print(s.solve("100+100"))
