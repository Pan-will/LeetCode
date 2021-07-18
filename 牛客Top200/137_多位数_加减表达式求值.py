"""
操作数不是个位数，比如100+100
且仅支持加减法

思路：先遍历字符串，将操作数用list存放，这样再遍历list即可
"""


class Solution:
    def str_to_list(self, string):
        if not string:
            return None
        res = []
        i = 0
        while i < len(string):
            tem = 0
            if not string[i].isdigit():
                res.append(string[i])
                i += 1
                continue
            while i < len(string) and string[i].isdigit():
                tem = tem * 10 + int(string[i])
                i += 1
            res.append(tem)
        print("str 2 list is:", res)
        return res

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
            return None
        # 将字符串转成list，为了适应多为操作数
        new_s = self.str_to_list(s)
        stack = []
        for ch in new_s:
            if ch == "(":
                stack.append(ch)
            elif ch == "+" or ch == "-" or ch == "*":
                stack.append(ch)
            elif type(ch) == int:
                stack.append(ch)
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
    print(s.solve("((10+2)*10-(100-(10+20*10-(2*3)))*10*1*2)-2"))
