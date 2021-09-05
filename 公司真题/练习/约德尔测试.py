"""
黑默丁格曾经提出了一个约德尔测试，将约德尔人的历史的每个阶段都用一个字符表达出来。
(包括可写字符,不包括空格。)。然后将这个字符串转化为一个01串。
转化规则是如果这个字符如果是字母或者数字，这个字符变为1,其它变为0。
然后将这个01串和黑默丁格观测星空得到的01串做比较，得到一个相似率。
相似率越高,则约德尔的未来越光明。
请问:相似率为多少？

输入：
@!%12dgsa
010111100

输出：
66.67%
"""
def getAns1():
    tar = input()
    god = input()
    count = 0
    for i, ch in enumerate(tar):
        if god[i] == "1":
            if ch.isalnum():
                count += 1
        else:
            if not ch.isalnum():
                count += 1
    print("%.2f" % (count / len(tar) * 100))

def getAns2():
    tar = list(input())
    god = list(input())
    count = 0
    for i, ch in enumerate(tar):
        if ch.isalnum():
            tar[i] = '1'
        else:
            tar[i] = '0'
    for t,g in zip(tar, god):
        if t == g:
            count += 1
    print("%.2f%%" % (count / len(tar) * 100))
    print("%.2f%%" % (count / float(len(tar)) * 100))

getAns2()
"""
*814cCRz>6qyasM"J,*v83=&^l1ZXczxO[v9-##RB5*/]hd=>J4@
0101010101010101010110101010101010101010101010101101
"""