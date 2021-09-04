"""
一场考试包含3道开放性题目，假设他们的难度从小到大分别为a, b, c，我们希望这3道题能满足下列条件：
a＜= b＜= c
b - a＜= 10
c - b＜= 10
所有出题人一共出了n道开放性题目。
现在我们想把这n道题分布到若干场考试中（1场或多场，每道题都必须使用且只能用一次），
然而由于上述条件的限制，可能有一些考试没法凑够3道题，
因此出题人就需要多出一些适当难度的题目来让每场考试都达到要求。
然而我们出题已经出得很累了，你能计算出我们最少还需要再出几道题吗？

样例输入
4
20 35 23 40
样例输出
2
"""


class S(object):
    def getAns(self, ques, num):
        ques = sorted(ques)
        print("升序排列：", ques)
        add = 0
        for i in range(num - 1):
            if ques[i + 1] - ques[i] <= 10:
                continue
            if ques[i + 1] - ques[i] <= 20 and ques[i + 1] - ques[i] > 10:
                add += 1
                continue
            if ques[i + 1] - ques[i] > 20:
                add += 2
                continue

        ad = (num + add) % 3
        if ad == 0:
            print(add)
        else:
            add += (3 - ad)
            print(add)

    def getAns2(self, nums, n):
        if n < 3:
            return 3 - n
        nums.sort()
        tar = 0
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 10:
                continue
            if 10 < nums[i + 1] - nums[i] <= 20:
                tar += 1
                continue
            if nums[i + 1] - nums[i] > 20:
                tar += 2
                continue
        extra = (tar + n) % 3
        if extra == 0:
            return tar
        else:
            return tar + 3 - extra


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    s = S()
    s.getAns(nums, n)
    print(s.getAns2(nums, n))
