# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]

    def twoSum2(self, numbers, target):
        temp = numbers
        temp.sort()
        print(temp, numbers)
        i, j = 0, len(numbers) - 1
        while i < j:
            if temp[i] + temp[j] < target:
                i += 1
            elif temp[i] + temp[j] > target:
                j -= 1
            else:
                print(numbers)
                a = numbers.index(temp[i])
                b = numbers.index(temp[j])
                print(temp[i], temp[j], a, b)
                return [a + 1, b + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
