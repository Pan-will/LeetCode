#
# 验证IP地址
# @param IP string字符串 一个IP地址字符串
# @return string字符串
#
class Solution:
    def isIpv4(self, chs):
        n = len(chs)
        ans = 0
        for ch in chs:
            if not ch.isdigit(): return False
            ans = ans * 10 + int(ch)
        if ans > 255:
            return False
        else:
            return True

    # 0不能连在一起
    def judge(self, chs):
        if len(chs) < 2:
            return True
        a = set(chs)
        b = list(a)
        if len(a) == 1 and b[0] == "0":
            return False
        return True

    def isIpv6(self, chs):
        n = len(chs)
        for ch in chs:
            if ch.islower():
                if ch > "f": return False
            elif ch.isupper():
                if ch > "F": return False
        # 0不能连在一起
        if not self.judge(chs): return False
        return True

    def solve(self, IP):
        # write code here
        if not IP:
            return "Neither"
        if "." in IP:
            arr = IP.split(".")
            if len(arr) != 4: return "Neither"
            for item in arr:
                if item == "" or item[0] == "0" or len(item) > 3 or not self.isIpv4(item): return "Neither"
            return "IPv4"
        else:
            arr = IP.split(":")
            if len(arr) != 8: return "Neither"
            for item in arr:
                if item == "" or len(item) > 4 or not self.isIpv6(item): return "Neither"
            return "IPv6"


if __name__ == '__main__':
    s = Solution()
    print(s.solve("172.16.254.1"))
