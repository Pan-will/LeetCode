"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
输入: "hello"
输出: "holle"

思路：双指针
注：要加好指针的判断，不能越界。
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 元音字母集合
        love = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # 将原串转成集合，方便交换元素
        lists = list(s)
        # print(lists)
        i = 0
        j = len(lists) - 1
        while i < j:
            if i < j and lists[i] not in love:
                i += 1
            if i < j and lists[j] not in love:
                j -= 1
            # 当i、j指向的元素都是元音时才交换
            if i < j and lists[i] in love and lists[j] in love:
                lists[i], lists[j] = lists[j], lists[i]
                i += 1
                j -= 1
        return ''.join(lists)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseVowels("leetcode"))
    print(solution.reverseVowels("hello"))
    print(solution.reverseVowels("a.b,."))
