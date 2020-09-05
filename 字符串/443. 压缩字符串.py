"""
给定一组字符，使用原地算法将其压缩。
压缩后的长度必须始终小于或等于原数组长度。
数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
在完成原地修改输入数组后，返回数组的新长度。

示例 1：
输入：["a","a","b","b","c","c","c"]
输出：返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]
说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。

思路：
遍历list：
如果下一个元素和当前元素一样，ans不变，计数器加一；
如果下一个元素和当前元素不一样，将ans和计数器转型后拼接到结果串后面；然后 ans重置，计数器重置；
"""


class Solution(object):
    def compress3(self, chars):
        # 设定记录元素的指针 和 写指针
        anchor = write = 0
        # 遍历原list
        for read, c in enumerate(chars):
            # 如果读到了原list末尾，或者当前字符与后一个字符不同，说明读到了相同字符的末尾
            if read + 1 == len(chars) or chars[read + 1] != c:
                # 将记录的元素写到新list中
                chars[write] = chars[anchor]
                # 写指针后移
                write += 1
                # 如果读指针比记录指针走得远
                if read > anchor:
                    # 将计数器字符化并拼接到新list后
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                # 记录指针赋新值
                anchor = read + 1
        res = [0]*write
        for k in range(write):
            if k<write:
                res[k] = chars[k]
        print(res)
        # 返回写指针的位置，即是新list的长度
        return write

    def compress2(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # 写指针
        ans = 0
        # 记录指针
        index = 0
        # 遍历原list
        for i, ch in enumerate(chars):
            # 要是遍历到了list的最后或者当前字符与下一个字符不同，则相同字符读取结束
            if i == len(chars) - 1 or chars[i + 1] != ch:
                # 将记录指针指向的元素赋给新list
                chars[ans] = chars[index]
                # 写指针后移
                ans += 1
                # 要是读指针走在记录指针的前面
                if i > index:
                    # 计算相同字符的长度
                    length = i - index + 1
                    for j in str(length):
                        chars[ans] = j
                        ans += 1
                index = i + 1
        result = [0] * ans
        for k in range(ans):
            if k < ans:
                result[k] = chars[k]
        print(result)
        return ans

    """
    将整数index按位拼接到集合后面
    """

    def intToList(self, result, index):
        """
        :type result: List[str]
        :type index: int
        :rtype: List[str]
        """
        temp = str(index)
        for i in range(len(temp)):
            result.append(temp[i])
        return result

    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        print("集合的长度：", len(chars))
        # 计数器初始化
        index = 1
        # 结果list的长度
        listLen = 1
        for i in range(1, len(chars)):
            # print(chars[i])
            if chars[i] == chars[i - 1]:
                index += 1
            elif chars[i] != chars[i - 1]:
                chars[listLen] = str(index)
                listLen += 1
                chars[listLen] = chars[i]
                listLen += 1
                index = 1
        print(chars)
        return listLen


if __name__ == '__main__':
    solution = Solution()
    print(solution.compress2(["a"]))
    print(solution.compress2(["a", "a", "b", "b", "c", "c", "c"]))
    print(solution.compress2(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
