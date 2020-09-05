class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        begin, end = 0, len(s) - 1
        while begin < end:
            if not s[begin].isalnum():
                begin += 1
                continue
            elif not s[end].isalnum():
                end -= 1
                continue
            elif s[begin].lower() != s[end].lower():
                return False
            begin += 1
            end -= 1
        return True

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        list = []
        # 记录list的长度
        size = 0
        # 遍历原字符串，将其中的字母转成小写格式放到list中
        for i in range(len(s)):
            if s[i].isalnum():
                list.append(s[i].lower())
                size += 1
            else:
                continue
            i += 1

        begin = 0
        end = len(list) - 1
        while begin < end:
            if list[begin] != list[end]:
                return False
            begin += 1
            end -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome2("A man, a plan, a canal: Panama"))
