import re


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        length = len(strs)  # 取得list的长度
        if length == 1:
            print(strs[0])
            return strs[0]

        strs.sort(key=len)  # 根据列表中的字符串长度排序
        ans = ''  # 返回值
        for i in range(len(strs[0])):  # 以列表中长度最小的单词为基准进行遍历
            for j in strs:  # 遍历列表中的每个字符串
                if j[i] != strs[0][i]:  # 如果列表中的字符串的对应下标是否相同
                    return ans
            else:
                ans += strs[0][i]  # 如果所有字符串下标都相同，更新最长公共前缀
        return ans

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        length = len(strs)  # 取得list的长度
        # print("list长度：", length)
        if length == 1:
            print(strs[0])
            return strs[0]

        ans = ""
        ans = Solution().commonPrefix(strs[0], strs[1])
        i = 1
        if i == length:
            print(ans)
            return ans
        else:
            ans = Solution().commonPrefix(ans, strs[i])
            # print(ans)
            i += 1
        print(ans)

    # 比较两个字符串的最长前缀
    def commonPrefix(self, str0, str1):
        if str0 == '': return str1
        if str1 == '': return str0
        if str0 == str1: return str0
        len0 = len(str0)
        len1 = len(str1)
        h = min(len0, len1)
        ans = ''
        i = 0
        j = 0
        # for k in range(length):
        if str0[i] == str1[j]:
            ans += str0[i]
            i += 1
            j += 1
        else:
            return ans


if __name__ == '__main__':
    solution = Solution()
    pattern = r'"|,'  # 定义分隔符
    url = input()  # 需要拆分的字符串
    result = re.split(pattern, url)
    result = [x for x in result if x != '']
    length = len(result)
    result.pop(length - 1)
    result.pop(0)
    solution.longestCommonPrefix(result)
