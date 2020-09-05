"""
给你一个整数 n 。请你先求出从 1 到 n 的每个整数 10 进制表示下的数位和（每一位上的数字相加），
然后把数位和相等的数字放到同一个组中。
请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。

示例 1：
输入：n = 13
输出：4
解释：总共有 9 个组，将 1 到 13 按数位求和后这些组分别是：
[1,10]，[2,11]，[3,12]，[4,13]，[5]，[6]，[7]，[8]，[9]。总共有 4 个组拥有的数字并列最多。

思路：
用两个list或字典。
"""

class Solution(object):
    # 用两个list
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 存放不同的数位和
        listkey = []
        # 统计各个数位和的个数
        listvalue = []
        for i in range(1, n + 1):
            # 存放数位和
            sumeve = 0
            temp = i
            # 计算每个数十进制的数位和
            while temp > 0:
                sumeve += temp % 10
                temp = int(temp / 10)
            # 若该数的数位和没出现过，则新增到listkey中，listvalue对应的计数置为1
            if sumeve not in listkey:
                listkey.append(sumeve)
                listvalue.append(1)
            # 若该数位和出现过，则在listkey中取得对应下标，在listvalue对应的计数加1
            else:
                listvalue[listkey.index(sumeve)] += 1
        # 统计并列最多的组
        res = 0
        for ch in listvalue:
            if ch == max(listvalue):
                res += 1
        return res

    # 用字典
    def countLargestGroup2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 统计各个数位和(key)及其个数(value)
        dict = {}
        for i in range(1, n + 1):
            # 存放数位和
            sumeve = 0
            temp = i
            # 计算每个数十进制的数位和
            while temp > 0:
                sumeve += temp % 10
                temp = int(temp / 10)
            # 若该数的数位和没出现过，则新增到字典中
            if sumeve not in dict.keys():
                dict[sumeve] = 1
            # 若该数位和出现过，则字典中value加1
            else:
                dict[sumeve] += 1
        # 统计并列最多的组
        res = 0
        for ch in dict.values():
            if ch == max(dict.values()):
                res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countLargestGroup2(13))
