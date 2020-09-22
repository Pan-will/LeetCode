import math


class Solution():

    def demo(self, num):
        nums.append(num)
        temp = []
        while num:
            temp.append(int(num % 10))
            num = num // 10
        sum = 0
        for item in temp:
            sum += int(math.pow(item, 2))
        if sum == 1:
            return True
        if sum in nums:
            return False
        nums.append(sum)
        return self.demo(sum)


if __name__ == '__main__':
    s = Solution()
    nums = []
    print(s.demo(19))
    print(s.demo(2))
