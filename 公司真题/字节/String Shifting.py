"""
我们规定对一个字符串的shift操作如下：
shift(“ABCD”, 0) = “ABCD”
shift(“ABCD”, 1) = “BCDA”
shift(“ABCD”, 2) = “CDAB”

换言之, 我们把最左侧的N个字符剪切下来, 按序附加到了右侧。
给定一个长度为n的字符串，我们规定最多可以进行n次向左的循环shift操作。
如果shift(string, x) = string (0＜= x ＜n), 我们称其为一次匹配(match)。
求在shift过程中出现匹配的次数。

样例输入
"byebyebye"

样例输出
3
"""

# 思路：
# 遍历字符串，每一次shift判断是否与原串相等。
# 判断同时维护一个计数器。
# 最后返回计数器的值。
class S(object):
    def getAns(self, arrs):
        n = len(arrs)


        pass


if __name__ == '__main__':
    ori = input()
    s = S()
    s.getAns(ori)
