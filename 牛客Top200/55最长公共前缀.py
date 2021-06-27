#
#
# @param strs string字符串一维数组
# @return string字符串
#         int length = strs[0].length();
#         int count = strs.length;
#         for (int i = 0; i < length; i++) {
#             char c = strs[0].charAt(i);
#             for (int j = 1; j < count; j++) {
#                 if (i == strs[j].length() || strs[j].charAt(i) != c) {
#                     return strs[0].substring(0, i);
#         return strs[0];
#
class Solution:
    # 思路：每个元素设一个指针，分别遍历每个元素，都相同则res+1，否则返回res.
    def longestCommonPrefix(self, strs):
        # write code here
        # 返回值
        res = ""
        if not strs:
            return res
        if len(strs) == 1: return strs[0]
        # 垂直遍历
        size = len(strs[0])
        num = len(strs)
        for i in range(size):
            temp = strs[0][i]
            for j in range(num):
                if i == len(strs[j]) or strs[j][i] != temp:
                    return strs[0][0:i]
        return strs[0]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["abca", "abc", "abca", "abc", "abcc"]))
