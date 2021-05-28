class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        chs = []
        index = 0
        # 记录添加的“-”个数
        num = 0
        for ch in number:
            if index == 3:
                chs.append("-")
                num += 1
                index = 0
            if ch != " " and ch != "-":
                chs.append(ch)
                index += 1
        # 记录数字个数
        newStr = "".join(chs)
        newList = newStr.split("-")
        print(newList)
        if len(newList) > 1 and len(newList[-1]) == 1:
            subStr = newList[-2] + newList[-1]
            if len(newList) == 2:
                return subStr[0:2] + "-" + subStr[2:]
            else:
                return "-".join(newList[:-2]) + "-" + subStr[0:2] + "-" + subStr[2:]
        else:
            res = "-".join(newList)
            print(res)
            if res[-1] == "-":
                return res[:-1]
            else:
                return res


if __name__ == '__main__':
    s = Solution()
    print(s.reformatNumber("1-23-45 6"))
