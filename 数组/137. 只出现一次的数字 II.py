"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,3,2]
输出: 3

示例 2:
输入: [0,1,0,1,0,1,99]
输出: 99
"""


class Solution(object):
    # 数学法思路：题中说其他元素均出现三次。
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3 * sum(list(set(nums))) - sum(nums)) // 2

    # 思路：遍历nums，用字典记录每个元素的次数，遍历字典返回value为1对应的key。
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for item in nums:
            if item in mydict.keys():
                mydict[item] += 1
            else:
                mydict[item] = 1
        for k, v in mydict.items():
            if v == 1:
                return k

    # 思路：先转set去重，然后遍历set返回在原list中只出现一次的元素。
    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newlist = list(set(nums))
        for item in newlist:
            if nums.count(item) > 1:
                continue
            else:
                return item


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
