"""
输入：
5 2 1 2
4 4 2 4 4

输出：6
有5个烽火台，2名将军，将军的影响范围为1，提升战斗力的值为2。
令将军驻守在第2和第4个烽火台，这样所有烽火台的战斗力都是6。
"""
class S(object):
    def getAns(self, nums, n, m, x, k):
        if n < 1: return 0
        if m < 1: return min(nums)



if __name__ == '__main__':
    n, m, x, k = input().split(" ")
    n, m, x, k = int(n), int(m), int(x), int(k)
    nums = input().split(" ")
    for i, num in enumerate(nums):
        nums[i] = int(num)
    s = S()
    print(s.getAns(nums, n, m, x, k))
