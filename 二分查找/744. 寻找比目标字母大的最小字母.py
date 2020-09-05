"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。
另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
在比较时，字母是依序循环出现的。举个例子：
如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

示例：
输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"
"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        letters = list(set(letters))
        letters.sort()
        if target in letters:
            index = letters.index(target)
            if index < len(letters) - 1:
                return letters[(index % len(letters)) + 1]
            if index == len(letters) - 1:
                return letters[(index + 1) % len(letters)]
        l, r = 0, len(letters) - 1
        while l < r:
            mid = int(l + (r - l) / 2)
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
        if l == len(letters) - 1 and letters[-1] < target:
            return letters[(l + 1) % len(letters)]
        else:
            return letters[l % len(letters)]

    def nextGreatestLetter2(self, letters, target):
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand


if __name__ == '__main__':
    solution = Solution()
    # print(solution.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e"))
    print(solution.nextGreatestLetter(["c", "f", "j"], "c"))
