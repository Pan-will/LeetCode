"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 返回值
        ans = []
        myDict = {}
        # 先转set去个重，此举完全是为了过用例，避免超时
        a = set(nums)
        # 统计每个元素的数量
        for item in a:
            myDict[item] = nums.count(item)
        # 将字典按元素个数排序（即按字典中的value降序）
        sorted_nums = sorted(myDict.items(), key=lambda x: x[1], reverse=True)
        # 计数器，直返回前k个
        index = 0
        for key, val in sorted_nums:
            if index < k:
                ans.append(key)
            else:
                break
            index += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
