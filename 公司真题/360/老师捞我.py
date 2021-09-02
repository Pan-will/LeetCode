"""
输入样例
2 20 80
51 50

输出样例
1

样例中，两名同学，第一位同学因为考试成绩高于第二位同学，故平时分也需要高于第二位同学；
假设第一位同学平时分为100分，第二位同学最高只能得到99分的平时分，无论如何都无法及格。
"""


class S(object):
    def getAns(self, scores, n, p, q):
        if n < 1: return 0
        scores.sort(reverse=True)
        res = 0
        i = 0
        if scores[i] >= 60:
            while scores[i] >= 60:
                res += 1
                i += 1
        if i == n: return res
        extra = 100 - i  # 此时平时分的最高分数
        for i in range(i, n):
            if (extra * p + scores[i] * q)/100 >= 60:
                res += 1
            extra -= 1  # 保证期末成绩高的平时分也高
        return res


if __name__ == '__main__':
    n, p, q = input().split(" ")
    n, p, q = int(n), int(p), int(q)
    scores = input().split(" ")
    for i, num in enumerate(scores):
        scores[i] = int(num)
    s = S()
    print(s.getAns(scores, n, p, q))
