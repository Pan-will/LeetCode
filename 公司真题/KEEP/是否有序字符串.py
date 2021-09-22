class S(object):
    # 题目规定cell字符串长度大于0
    def solve(self, cell):
        n = len(cell)
        if n < 2:
            return True
        ori = list(cell)
        zcell = sorted(ori)  # 字典升序
        zcell_i = 1  # 遍历升序字符
        in_a = ori.index('a')  # 先找到a的下标
        print("原串中a的下标为：", in_a)
        if in_a == 0:
            return cell == "".join(zcell)
        elif in_a == n-1:
            return cell[::-1] == "".join(zcell)
        i, j = in_a - 1, in_a + 1
        while zcell_i < n:
            if ori[i] == zcell[zcell_i]:
                i -= 1
            elif ori[j] == zcell[zcell_i]:
                j += 1
            else:  # 若前后都没有字符与当前字符相等，则不是有序字符串，返回false
                return False
            zcell_i += 1
        if i == -1 and j == n:
            return True


if __name__ == '__main__':
    s = S()
    print(s.solve("ihfcbadeg"))
    print(s.solve("bca"))
