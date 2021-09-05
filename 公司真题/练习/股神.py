"""
经过严密的计算，小赛买了一支股票，他知道从他买股票的那天开始，股票会有以下变化：
第一天不变，以后涨一天，跌一天，涨两天，跌一天，涨三天，跌一天...依此类推。
为方便计算，假设每次涨和跌皆为1，股票初始单价也为1，请计算买股票的第n天每股股票值多少钱？

样例输入
1 2 3 4 5

样例输出
1 2 1 2 3
"""
def getAns(num):
    sum = 0
    for i in range(2, n+1):
        if num <= sum + i and num > sum:
            print(num - (i-2) * 2)
            break
        else:
            sum += i

def getRes(n):
    recPri = []
    while n < 3:
        print(n)
        return
    day = 0  # 一轮开始之前
    up = 1  # 当前轮连涨带跌的天数，初始化为第一轮
    while len(recPri) < n:
        if day < up:
            recPri.append(1)
            day += 1
        elif day == up:  # 每涨完一轮，会跌一天
            recPri.append(-1)
            up += 1  # 下一轮涨的天数也递增1天
            day = 0  # 重新记录天数
    print("长度：", len(recPri), "涨跌趋势：", recPri)
    price = [1] + [0 for _ in range(n - 1)]
    for i in range(1, n):
        price[i] = price[i - 1] + recPri[i - 1]
    print("长度：", len(price), "股票价格：", price)
    print(price[-1])


if __name__ == '__main__':
    while 1:
        n = int(input())
        getRes(n)
        getAns(n)
