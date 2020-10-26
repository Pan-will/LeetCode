"""
示例 1：

输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释：
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。
对于 nums[3]=2 存在一个比它小的数字：（1）。
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
"""


class Solution(object):
    # 用字典
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mydict = {}
        temp = []
        for i, v in enumerate(nums):
            temp.append(i)
            if v in mydict.keys():
                mydict[v] += temp
            else:
                mydict[v] = temp
            temp = []
        newList = sorted(mydict.items(), key=lambda item: item[0], reverse=True)
        # print(newList)
        # 记录原list的元素个数
        count = len(nums)
        ans = [0 for _ in range(count)]
        for i in range(len(newList)):
            # 同值元素的下标
            indexList = newList[i][1]
            # 更新计数器
            count -= len(indexList)
            # 同值元素的结果相同
            for index in indexList:
                ans[index] = count
        return ans


    # 暴力法
    def smallerNumbersThanCurrent2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums:
            ans.append(self.smallCount(nums, i))
        return ans

    # 统计数组中比n小的数的个数
    def smallCount(self, nums, n):
        if not nums:
            return 0
        ans = 0
        for item in nums:
            if item < n:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
