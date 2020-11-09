"""
我们有一个项的集合，其中第 i 项的值为 values[i]，标签为 labels[i]。

我们从这些项中选出一个子集 S，这样一来：

|S| <= num_wanted
对于任意的标签 L，子集 S 中标签为 L 的项的数目总满足 <= use_limit。
返回子集 S 的最大可能的 和。

示例 1：
输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
输出：9
解释：选出的子集是第一项，第三项和第五项。

示例 2：
输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
输出：12
解释：选出的子集是第一项，第二项和第三项。

示例 3：
输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
输出：16
解释：选出的子集是第一项和第四项。
"""


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        # 1:用字典，按标签统计所有值
        mydict = {}
        i = 0
        n = len(labels)
        while i < n:
            if labels[i] in mydict.keys():
                mydict[labels[i]].append(values[i])
            else:
                mydict[labels[i]] = [values[i]]
            i += 1
        # 遍历字典，每个标签中取出use_limit个数放到res中
        res = []
        for item in mydict.values():
            item.sort(reverse=True)
            res += item[:use_limit]
        # res降序排，返回sum(res[:num_wanted])
        res.sort(reverse=True)
        return sum(res[:num_wanted])


if __name__ == '__main__':
    s = Solution()
    print(s.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 3, 3, 3, 2], num_wanted=3, use_limit=2))
