"""
组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。

然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。
如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。

给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。
请你返回 所有可能的无矛盾球队中得分最高那支的分数 。

示例 1：
输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
输出：34
解释：你可以选中所有球员。
"""


class Solution(object):
    # 首先要无矛盾，其次要得分最高
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        mydict = {}
        for i in range(len(ages)):
            mydict[ages[i]] = scores[i]
        # 按得分将字典排序
        sorted(mydict.items(), key=lambda d: d[1])
        ages = mydict.keys()
        scores = mydict.values()
        res = 0



if __name__ == '__main__':
    s = Solution()
    print(s.bestTeamScore(scores=[1, 3, 5, 10, 15], ages=[1, 2, 3, 4, 5]))
