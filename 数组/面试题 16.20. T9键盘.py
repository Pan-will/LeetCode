"""
在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。
每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。
你会得到一张含有有效单词的列表。

示例 1:
输入: num = "8733", words = ["tree", "used"]
输出: ["tree", "used"]

示例 2:
输入: num = "2", words = ["a", "b", "c", "d"]
输出: ["a", "b", "c"]
"""


class Solution(object):
    def getValidT9Words(self, num, words):
        """
        :type num: str
        :type words: List[str]
        :rtype: List[str]
        """
        my_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        tempList = []
        for ch in num:
            tempList.append(my_dict[ch])
        # 遍历单词表
        for word in words:
            if len(word) != len(num):
                continue
            # 遍历单词中的每个字符
            i = 0
            for ch in word:
                if ch not in tempList[i]:
                    break
                if ch in tempList[i]:
                    i += 1
            if i == len(word):
                res.append(word)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.getValidT9Words(num="8733", words=["tree", "used"]))
    print(solution.getValidT9Words(num = "2", words = ["a", "b", "c", "d"]))
