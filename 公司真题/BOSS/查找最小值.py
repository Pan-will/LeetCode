# @param randomData long长整型 一个随机数字
# @return long长整型
#
class Solution:
    def smallest(self, randomData):
        tem = str(randomData)
        tar = []
        for i in tem:
            tar.append(int(i))
        print(tar)
        min_val = min(tar)
        min_index = 0
        temp = tar[::-1]
        print(temp)
        for i, num in enumerate(temp):
            if num == min_val:
                min_index = i
        tar.pop(min_index)
        tar = [min_val] + tar
        print(tar)


if __name__ == '__main__':
    s = Solution()
    print(s.smallest(261235))
