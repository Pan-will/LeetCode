"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
解释：
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

思路：
1、递归，参数n是递归趟数
2、初始字符串是：“1”，用ans字符串存放结果
3、遍历字符串，变量tar记录遇到的字符，变量index记录tar出现的次数
    ————当指针指向的字符与tar相同时，将index自增1；
    ————当指针指向的字符与tar不同时，将index和tar添加到ans的末尾。
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 第一趟结果已知，不参与循环
        result = "1"
        n -= 1
        # 循环n-1趟
        while n > 0:
            # 初始化拼接字符串
            ans = ""
            # 记录当前字符,初始为原串首字符
            tar = result[0]
            # 计数器
            count = 1
            # 遍历原串，拼接结果字符串
            for i in range(1, len(result)):
                # 指针指向的字符等于记录字符，计数器加1
                if result[i] == tar:
                    count += 1
                # 不相等，拼接结果串，并在之后重置记录字符、计数器
                else:
                    # 字符串拼接
                    ans += str(count) + tar
                    # 重置
                    tar = result[i]
                    count = 1
            # 字符串拼接
            ans += str(count) + tar
            # 重置原字符串
            result = ans
            # 循环趟数减1
            n -= 1
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(1))
    print(solution.countAndSay(2))
    print(solution.countAndSay(3))
    print(solution.countAndSay(4))
