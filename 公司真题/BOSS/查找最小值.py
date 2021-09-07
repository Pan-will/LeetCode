# @param randomData long长整型 一个随机数字
# @return long长整型
#
class Solution:
    def smallest(self, randomData):
        tem = str(randomData)
        tar = []
        for i in tem:
            tar.append(int(i))
        min_val = min(tar)
        min_index = tar.index(min_val)
        for i in range(min_index, len(tar)):
            if tar[i] == min_val:
                min_index = i
        tar.pop(min_index)
        tar = [min_val] + tar
        res = 0
        for num in tar:
            res = res * 10 + num
        print(res)


if __name__ == '__main__':
    s = Solution()
    s.smallest(261235)
    s.smallest(100000)
