class S():
    def solve(self, cell, m):
        if not cell:
            return False
        ori = list(cell)
        n = len(ori)
        print(cell)
        while m > 0:
            m -= 1
            # 先找出本轮要操作的1的位置
            index1 = []
            for i, ch in enumerate(ori):
                if ch == '1':
                    index1.append(i)
            for i in index1:
                if 0 < i < n - 1:
                    ori[i - 1] = '1'
                    ori[i + 1] = '1'
                elif i == 0:
                    ori[i + 1] = '1'
                elif i == n - 1:
                    ori[i - 1] = '1'
        return "".join(ori)


if __name__ == '__main__':
    s = S()
    print(s.solve("0100000000001", 3))
