"""
密码生成器由N个槽位组成，槽位的下标为0~N-1，每个槽位存储一个数。起初每个槽位都是0。
密码生成器会进行M轮计算，每轮计算，小汪会输入两个数L,R(L<=R),密码生成器会将这两个数作为下标，将两个下标之间（包含）的所有槽位赋值为i（i为当前的轮次，i∈[1,M]）。
M轮计算完成后，密码生成器会根据槽位的最终值生成一条密码，密码的生成规则为：
（0*a[0] + 1*a[1] + 2*a[2] + ... + (N-1)*a[N-1]) mod 100000009
其中a[i]表示第i个槽位的最终值。
请帮助小汪把他的密码生成器实现为代码。

输入描述:
第一行为两个整数N,M,表示槽位个数和计算轮数。
接下来M行，每行两个整数Li,Ri，表示第i轮计算的输入。

输出描述:
输出一行，一个整数A,表示小汪的开机密码。

输入例子1:
5 3
2 3
1 2
1 1

输出例子1:
10
"""


class Solution():
    def PasswordCreate(self, arr):
        M = [0] * arr[0][0]
        index = 1
        for begin, end in arr[1:]:
            for i in range(begin, end + 1):
                M[i] = index
            index += 1
        ans = 0
        for i in range(len(M)):
            ans += i*M[i]
        return ans % 100000009



if __name__ == '__main__':
    s = Solution()
    arr = [[5, 3], [2, 3], [1, 2], [1, 1]]
    print(s.PasswordCreate(arr))
