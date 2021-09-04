"""
给定一个长度为n的整数数组a，元素均不相同，
问数组是否存在这样一个片段，只将该片段翻转就可以使整个数组 升序排列。
"""


class S(object):
    def getAns(self, nums, n):
        oris = sorted(nums)
        comp = [nums[i] for i in range(n) if nums[i] != oris[i]]
        start = nums.index(comp[0])
        end = nums.index(comp[-1])
        if nums[:start] + nums[start:end+1][::-1] + nums[end+1:] == oris:
            return "yes"
        else:
            return "no"


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    s = S()
    print(s.getAns(nums, n))
