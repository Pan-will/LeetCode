# -*- coding:utf-8 -*-

class Solution:
    def trans(self, s, n):
        if n == 0: return ""
        arr = list(s)
        print("转换大小写前，arr：", arr)
        for i, ch in enumerate(arr):
            if ch == " ":
                continue
            else:
                arr[i] = ch.lower() if ch.isupper() else ch.upper()
        print("转换大小写后，arr：", arr)
        s = "".join(arr)
        print("arr转成字符串为：", s)
        words = s.split(" ")
        words = words[::-1]
        return " ".join(words)



if __name__ == '__main__':
    s = Solution()
    print(s.trans2("HeLlO World", 10))
