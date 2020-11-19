"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def __init__(self):
        self.res = []
        self.mydict = {1: "", 2: "abc", 3: "def",
                       4: "ghi", 5: "jkl", 6: "mno",
                       7: "pqrs", 8: "tuv", 9: "wxyz"}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 特判
        if not digits:
            return []
        # 将数字串转成list[int]类型
        nums = []
        for ch in digits:
            nums.append(int(ch))
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, cur, temp):
        # 定义递归出口：若临时串长度达到则找到一个新答案
        if cur == len(nums):
            self.res.append("".join(temp))
            return
        digits = self.mydict[nums[cur]]
        for digit in digits:
            temp.append(digit)
            self.dfs(nums, cur + 1, temp)
            temp.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
