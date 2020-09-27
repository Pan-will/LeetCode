"""
单调栈，类似题：496、901、42、84
"""
"""
请根据每日 气温 列表，重新生成一个列表。
对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例：
输入：temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
输出：[1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。
每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""


# 思路：注意题目说的是更高的气温，而不是最高的气温。
# 因此，只要找到原list中在当前元素后面且比当前元素大的位置的下标，赋值即可。
class Solution(object):
    # 单调栈。
    # 遍历T，维护一个栈，栈空或者当前元素比栈顶小，则入栈，否则栈顶出栈，并在res中记录栈顶元素位置的答案。
    # 注意栈中存放的应该是每个元素的下标。
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        lenT = len(T)
        # 返回值
        res = [0] * lenT
        stack = []
        for index, curT in enumerate(T):
            while stack and curT > T[stack[-1]]:
                temp = stack.pop()
                res[temp] = index - temp
            stack.append(index)
        return res

    # 暴力超时
    def dailyTemperatures2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        res = []
        for i in range(len(T)):
            temp = T[i:]
            if not temp:
                break
            for j in range(1, len(temp)):
                if temp[j] > T[i]:
                    res.append(j)
                    break
                if j == len(temp) - 1:
                    res.append(0)
                    break
        res.append(0)
        return res


if __name__ == '__main__':
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(temperatures))
