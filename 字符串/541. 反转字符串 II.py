"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转;
如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"

要求:
该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。

思路：
利用字符串截取函数str[a:b]
注：若b越界，只截取到原串末尾。

1、每趟原串舍弃前2K个字符；
2、截取前K个字符并反转
3、截取K--2K的字符
4、拼接2和3的结果并整体拼接到ans后；
5、当原串为空时结束循环，返回ans。
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lens = len(s)
        # 若原串长度小于k,则将原串反转返回
        if lens < k:
            return s[::-1]
        # 第二个参数越界则截取到串的最后一个字符，不多取空字符
        # return s[2*k:8*k]
        # 返回值
        ans = ""
        # 当原串不空时执行循环
        while not s == "":
            # 截取前K个
            temp = s[0:k]
            print("截取前K个字符：",temp)
            # 反转
            temp = temp[::-1]
            print("反转后：",temp)
            # 截取后K个
            flag = s[k:2 * k]
            print("截取后K个字符：",flag)
            # 拼接到结果串
            ans = ans + temp + flag
            print("拼接后：",ans)
            # 原串前2K个字符舍弃
            s = s[2 * k:]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseStr("abcdefg", 2))
    print(solution.reverseStr("abcdlaksgdcdefg", 3))
