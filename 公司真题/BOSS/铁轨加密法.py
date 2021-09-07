# @param data string字符串 加密数据
# @param n int整型 轨道数
# @return string字符串
#
class Solution:
    # 思路：滑动窗口，每次移动n-1个单位
    def railEncode(self, data, n):
        if not data:
            return ""
        size = len(data)
        if size <= n:
            return data
        res = [[] for _ in range(n)]
        # 偶数次正序放到res里

        # 奇数次要倒序放到res里

        # 格式化输入
        ans = ""
        for item in res:
            ans += "".join(item)
        print(ans)

    def railEncode2(self, data, n):
        if not data:
            return ""
        size = len(data)
        if size <= n:
            return data
        res = [[] for _ in range(n)]
        # 每遍历n个，指针要回退1
        cur = 0
        extra = size % n
        while cur < n + extra:
            temp = data[cur:cur + n]
            for ch, arr in zip(temp, res):
                arr.append(ch)
            cur += n
            if (cur + 1) % n == 0:
                cur -= 1
        print(res)
        ans = ""
        for item in res:
            ans += "".join(item)
        print(ans)


if __name__ == '__main__':
    s = Solution()
    data = "abcdefghijklmno"
    print(data[10: 20], len(data[10:20]))
    s.railEncode(data, 3)
