#
# 验证IP地址
# @param IP string字符串 一个IP地址字符串
# @return string字符串
#
class Solution:
    def isIpv4(self, chs):
        ans = 0
        for ch in chs:
            if not ch.isdigit(): return False
            ans = ans * 10 + int(ch)
        if ans > 255:
            return False
        else:
            return True

    def isIpv6(self, chs):
        for ch in chs:
            if ch.islower():
                if ch > "f": return False
            elif ch.isupper():
                if ch > "F": return False
        return True

    def solve(self, IP):
        # write code here
        if not IP:
            return "Neither"
        if "." in IP:
            arr = IP.split(".")
            if len(arr) != 4: return "Neither"
            for item in arr:
                if item == "" or (len(item) > 1 and item[0] == "0") or len(item) > 3 or not self.isIpv4(item): return "Neither"
            return "IPv4"
        else:
            arr = IP.split(":")
            if len(arr) != 8: return "Neither"
            for item in arr:
                if item == "" or len(item) > 4 or not self.isIpv6(item): return "Neither"
            return "IPv6"


if __name__ == '__main__':
    s = Solution()
    print(s.solve("192.0.0.1"))
    # print(s.solve("2001:0db8:85a3:0000:0:8A2E:0370:733a"))
