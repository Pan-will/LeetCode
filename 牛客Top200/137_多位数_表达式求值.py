"""
操作数不是个位数，比如100+100
支持加减乘除法。

思路：
1、遍历字符串，将操作数用list存放；
2、利用栈，将list存放的中缀表达式转成后缀表达式；
3、后缀表达式求值即可。
"""


class Solution:
    def middle2behind(self, expression):
        result = []  # 结果列表
        stack = []  # 栈
        for item in expression:
            if item.isnumeric():  # 如果当前字符为数字那么直接放入结果列表
                result.append(item)
            else:  # 如果当前字符为一切其他操作符
                if len(stack) == 0:  # 如果栈空，直接入栈
                    stack.append(item)
                elif item in '*/(':  # 如果当前字符为*/（，直接入栈
                    stack.append(item)
                elif item == ')':  # 如果右括号则全部弹出（碰到左括号停止）
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                # 如果当前字符为加减且栈顶为乘除，则开始弹出
                elif item in '+-' and stack[len(stack) - 1] in '*/':
                    if stack.count('(') == 0:  # 如果有左括号，弹到左括号为止
                        while stack:
                            result.append(stack.pop())
                    else:  # 如果没有左括号，弹出所有
                        t = stack.pop()
                        while t != '(':
                            result.append(t)
                            t = stack.pop()
                        stack.append('(')
                    stack.append(item)  # 弹出操作完成后将‘+-’入栈
                else:
                    stack.append(item)  # 其余情况直接入栈（如当前字符为+，栈顶为+-）

        # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
        while stack:
            result.append(stack.pop())
        return result

    # 字符串表示的中缀表达式转用list存放——为了适应多位数运算
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

    # 将list存放的前缀表达式转成后缀表达式
    """
    1.遇到操作数，直接输出； 
    2.栈为空时，遇到运算符，入栈； 
    3.遇到左括号，将其入栈； 
    4.遇到右括号，执行出栈操作，并将出栈的元素输出，直到弹出栈的是左括号，左括号不输出； 
    5.遇到其他运算符’+”-”*”/’时，弹出所有优先级大于或等于该运算符的栈顶元素，然后将该运算符入栈； 
    6.最终将栈中的元素依次出栈，输出。
    """

    def qian_to_hou(self, arr):
        if not arr:
            return None
        op_low = ["+", "-"]
        op_high = ["*", "/"]
        stack = []  # 用来存放操作符
        res = []  # 用来存放后缀表达式
        for item in arr:
            if type(item) == int:
                res.append(item)
            # 遇到运算符，且栈为空，则运算符直接入栈
            elif (item in op_low or item in op_high) and not stack:
                stack.append(item)
            # 遇到运算符，且栈不为空，则将栈顶元素优先级高的出栈
            elif item in op_low and stack:
                while stack and (stack[-1] in op_low or stack[-1] in op_high):
                    res.append(stack.pop(-1))
                stack.append(item)
            elif item in op_high and stack:
                while stack and stack[-1] in op_high:
                    res.append(stack.pop(-1))
                stack.append(item)
            # 遇到左括号，直接入栈
            elif item == "(":
                stack.append(item)
            # 遇到右括号，执行出栈操作，并将出栈的元素输出，直到弹出栈的是左括号，左括号不输出；
            elif item == ")":
                while stack and stack[-1] != "(":
                    res.append(stack.pop(-1))
                # 将左括号出栈，但不进入res
                stack.pop(-1)
        if stack:
            res.append(stack.pop(-1))
        return res

    def opera(self, b, op, a):
        if op == "+":
            return b + a
        elif op == "-":
            return b - a
        else:
            return b * a

    # 中缀转后缀，后缀表达式求值
    def solve(self, s):
        # 判空
        if not s:
            return None
        # 将字符串转成list，为了适应多为操作数
        new_s = self.str_to_list(s)
        new_s = self.qian_to_hou(new_s)
        stack = []
        for ch in new_s:
            if type(ch) == int:
                stack.append(ch)
            elif ch == "+" or ch == "-" or ch == "*":
                a = stack.pop(-1)
                op = ch
                b = stack.pop(-1)
                stack.append(self.opera(b, op, a))
        return stack[-1]


if __name__ == '__main__':
    s = Solution()
    string = "((10+2)*10-(100-(10+20*10-(2*3)))*10*1*2)-2"
    arr = s.str_to_list(string)
    print(s.qian_to_hou(arr))
    print(s.solve(string))
