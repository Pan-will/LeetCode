"""
给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。
数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。
在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。


示例 1：
输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。
"""


# 思路：用回溯法统计长度为k的子序列，用res记录下来; 遍历res返回最有竞争力的那个子序列。   -----超时
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 返回值初始化
        res = nums[:k]
        n = len(nums)
        # 通过回溯找到所有长为k的子序列
        self.dfs(res, nums, n, k, 0, [])
        # 遍历res找到最优竞争力的子序列
        # ans = res[0]
        # for i in range(1, len(res)):
        #     ans = self.betterPower(ans, res[i])
        # return ans
        return res

    def dfs(self, res, nums, n, k, begin, temp):
        # 定义递归出口：长度为k
        if len(temp) == k and temp != res and temp == self.betterPower(temp, res):
            res = temp
        for i in range(begin, n):
            if len(temp) > k:
                break
            self.dfs(res, nums, n, k, i + 1, temp + [nums[i]])

    # 返回两个序列中有竞争力的那个
    def betterPower(self, l1, l2):
        # 两个序列相同，任意返回一个
        if l1 == l2:
            return l1
        # 否则，返回有竞争力的那个
        else:
            temp = zip(l1, l2)
            for item in temp:
                if item[0] < item[1]:
                    return l1
                elif item[0] > item[1]:
                    return l2
                else:
                    continue


if __name__ == '__main__':
    s = Solution()
    print(s.mostCompetitive([3, 5, 2, 6], 2))
    # print(s.mostCompetitive(
    #     [84, 10, 71, 23, 66, 61, 62, 64, 34, 41, 80, 25, 91, 43, 4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61, 95, 71],
    #     24))
