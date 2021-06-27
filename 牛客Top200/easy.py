# 反转字符串
class fanzhuan:
    def solve(self, str):
        n = len(str)
        if n < 2:
            return str

        arr = ["a" for _ in range(n)]
        print(arr)
        i, j = 0, len(str) - 1
        while i <= j:
            arr[j], arr[i] = str[i], str[j]
            i += 1
            j -= 1
        return "".join(arr)

    def solve2(self, str):
        # write code here
        arr = list(str)
        arr = arr[::-1]
        return "".join(arr)


class Huiwen:
    def judge(self, str):
        n = len(str)
        if n < 2:
            return True
        i, j = 0, n - 1
        while i < j:
            if str[i] != str[j]:
                return False
            i += 1
            j -= 1
        return True


class test:
    def test1(self):
        print([i for i in range(5)])


if __name__ == '__main__':
    t = test()
    t.test1()
