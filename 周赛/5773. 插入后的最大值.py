class Solution(object):
    # 思路：
    # 若原数为负：插到从左往右第一个比x大的数字左边；
    # 若原数为正：插到从左往右第一个比x小的数字左边；
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        res = []
        if n[0] == "-":
            for i in range(1, len(n)):
                if ord(n[i]) - ord("0") > x:
                    res.append(n[:i])
                    res.append(str(x))
                    res.append(n[i:])
                    return "".join(res)
        else:
            for i in range(len(n)):
                if ord(n[i]) - ord("0") < x:
                    res.append(n[:i])
                    res.append(str(x))
                    res.append(n[i:])
                    return "".join(res)

        return n+str(x)


if __name__ == '__main__':
    s = Solution()
    print(s.maxValue("231", 2))
    print(s.maxValue(n="13", x=2))
    print(s.maxValue("-99", 9))
