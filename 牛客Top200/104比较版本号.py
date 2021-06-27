#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 比较版本号
# @param version1 string字符串
# @param version2 string字符串
# @return int整型
#
class Solution:
    # 思路：用.分割字符串，遍历字符串，每个元素转int类型，再比较大小即可。
    def compare(self, version1, version2):
        # write code here
        arra = version1.split(".")
        arrb = version2.split(".")
        n = len(arra) if len(arra) <= len(arrb) else len(arrb)
        for i in range(n):
            a = self.str2int(arra[i])
            b = self.str2int(arrb[i])
            if a > b:
                return 1
            elif a < b:
                return -1
        if len(arra) > len(arrb):
            arra = arra[n:]
            for item in arra:
                if self.str2int(item) > 0: return 1
            return 0
        elif len(arra) < len(arrb):
            arrb = arrb[n:]
            for item in arrb:
                if self.str2int(item) > 0: return -1
            return 0
        else:
            return 0

    def str2int(self, chs):
        if not chs:
            return 0
        ans = 0
        for ch in chs:
            ans = ans * 10 + int(ch)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.compare("1.01", "1.001"))
    print(s.compare("1.1", "2.1"))
    print(s.compare("2.0.1", "2"))
    print(s.compare("1.0", "1.0.0"))
