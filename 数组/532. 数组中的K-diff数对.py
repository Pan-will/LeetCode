"""
给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。
这里将 k-diff 数对定义为一个整数对 (i, j)：
    其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

示例 1:
输入: [3, 1, 4, 1, 5], k = 2
输出: 2
解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。

示例 2:
输入:[1, 2, 3, 4, 5], k = 1
输出: 4
解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。

注意:
数对 (i, j) 和数对 (j, i) 被算作同一数对。
数组的长度不超过10,000。
所有输入的整数的范围在 [-1e7, 1e7]。

思路：
想到：绝对值应是非负数，所以k<0的情况下要排除（测试用例有k<0的）；
设置计数器ans=0；
1、转set去重，再转回list，将newnums[]升序排列；
2、若k==0，则 2-diff 数对是相同元素对，所以遍历newnums,其中元素nums.count(newnums[i]) >= 2，ans加1；
3、若k>0，则 2-diff 数对是不同元素对，遍历newnums,若(newnums[i] + k)也在newnums中，则ans加1；
4、返回ans。
"""

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 绝对值应是非负数
        if k < 0:
            return 0
        # 转set去重，再升序排
        newnums = sorted(set(nums))
        ans = 0
        # 差为0，则是相同元素对
        if k == 0:
            for i in range(len(newnums)):
                if nums.count(newnums[i]) >= 2:
                    ans += 1
        # 差的绝对值大于0，则是不同元素对
        else:
            for i in range(len(newnums)):
                if newnums[i] + k in newnums:
                    ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPairs([1, 3, 1, 4, 5], 0))
