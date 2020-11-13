"""
森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。
这些回答放在 answers 数组里。返回森林中兔子的最少数量。

示例:
输入: answers = [1, 1, 2]
输出: 5
解释:
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

输入: answers = [10, 10, 10]
输出: 11

输入: answers = []
输出: 0
"""


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        mydict = {}
        for item in answers:
            if item in mydict.keys():
                mydict[item] += 1
            else:
                mydict[item] = 1
        # print(mydict)
        res = 0
        for k, v in mydict.items():
            res += ((v - 1) / (k + 1) + 1) * (k + 1)
        return int(res)


if __name__ == '__main__':
    s = Solution()
    print(s.numRabbits([0, 0, 1, 1, 1]))
    print(s.numRabbits([1, 0, 1, 0, 0]))
    # print(4 // 2)
