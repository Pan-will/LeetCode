#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算模板串S在文本串T中出现了多少次
# @param S string字符串 模板串
# @param T string字符串 文本串
# @return int整型
#
class Solution:
    def get_next(self, chs):
        """求模板串的next数组"""
        n = len(chs)
        next = [0]
        if n < 2:
            return next
        for i in range(1, n):
            # 从第二个字符开始处理；若只有一个字符，则不进入该循环
            temp = chs[0: i]  # 分片,得到用于计算next的子串
            lentemp = len(temp)  # lentemp是子串的长度
            if lentemp == 1:
                next.append(1)
            else:  # 如果子串不只一个字符
                num = 1  # 该处next的默认值
                j = lentemp - 1
                while j > 0:
                    if temp[0:j] == temp[lentemp - j: lentemp]:
                        num = j + 1
                        break
                    j -= 1
                next.append(num)
            i += 1
        return next

    def get_nextVal(self, chs, next):
        '''求模板串的nextVal数组'''
        nextval = next[:]  # 初始化nextval数组
        if (len(chs) >= 3):
            # 只有当字符串有三个及以上元素时，才有必要进行计算
            for i in range(2, len(chs)):  # 从第三个元素开始
                if (chs[i] == chs[next[i] - 1]):
                    nextval[i] = nextval[next[i] - 1]
        return nextval

    def kmp(self, S, T):
        lens = len(S)
        lent = len(T)
        # 判空
        if not S or not T or lens > lent:
            return 0
        # 求模式串的next数组
        nextArr = self.get_next(S)
        # print(nextArr)
        si, ti = 0, 0
        # 返回值
        res = 0
        # 用指针扫描文本串
        while ti < lent:
            if S[si] == T[ti]:
                if si == lens - 1:
                    res += 1
                    si = nextArr[si]
                    continue
                si += 1
                ti += 1
            else:
                si = nextArr[si]
        return res

    def kmp2(self, S, T):
        lens = len(S)
        lent = len(T)
        # 判空
        if not S or not T or lens > lent:
            return 0
        ans = 0
        for i in range(lent - lens + 1):
            if T[i: lens + i] == S:
                ans += 1
        return ans

    def myKmp(self, subStr, bigStr):
        if not bigStr: return None
        sizeSub = len(subStr)
        res = 0
        for i in range(len(bigStr)):
            if bigStr[i] == subStr[0]:
                if bigStr[i: i + sizeSub] == subStr:
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.kmp("ababab", "abababab"))
    print(s.myKmp("ababab", "ababab123456ababababab"))
