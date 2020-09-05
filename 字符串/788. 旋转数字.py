"""
称一个数 X 为好数：如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。
注意：要求每位数字都要被旋转。

如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。
0, 1, 和 8 被旋转后仍然是它们自己；
2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；
6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数。

示例：
输入: 10
输出: 4
解释:
在[1, 10]中有四个好数： 2, 5, 6, 9。
注意 1 和 10 不是好数, 因为他们在旋转之后不变。

思路：
1、遍历从1---N+1的所有整数
2、将当前数字转化成字符串ch，只有所有字符都是list1中的字符，才满足旋转条件；
3、遍历字符串化后的数，将存在list1中的字符旋转，拼接给ans；
4、旋转后比较ch和ans，相等则res加1；
5、返回res。
"""


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        list1 = ['0', '1', '8', '2', '5', '6', '9']
        res = 0
        # 遍历从1到N
        for i in range(1, N+1):
            # 整数字符串化，判断是否是旋转后不变化的数，是则进入下一趟循环
            if set(str(i)) <= {'0', '1', '8'}:
                print("旋转后不变的数：", i)
                continue
            # 转成字符串
            ch = str(i)
            ans = ""
            # 转成set
            setch = set(ch)
            # 操作旋转后会变的数
            if setch <= set(list1):
                print("旋转后会变,且符合旋转条件的数：", i)
                print("字符串化,且符合旋转条件的数：", ch)
                # 遍历字符串，按要求将对应的数字旋转
                for index, eng in enumerate(ch):
                    print("遍历字符串化后的数：当前字符为：", eng)
                    if eng in ['0', '1', '8']:
                        ans += eng
                    elif eng in ['2', '5'] and eng == '2':
                        ans += '5'
                    elif eng in ['2', '5'] and eng == '5':
                        ans += '2'
                    elif eng in ['6', '9'] and eng == '6':
                        ans += '9'
                    elif eng in ['6', '9'] and eng == '9':
                        ans += '6'
                    else:
                        ans += eng
                print("旋转后的数：", ans)
            # 不满足旋转条件的数跳过
            else:
                continue
            # 判断旋转前后是否相等，即是不是“好数”
            if ans != ch:
                print("满足条件的好数：", ch)
                res += 1
            print()
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotatedDigits(2))
    print(solution.rotatedDigits(10))
