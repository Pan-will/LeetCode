class Solution(object):
    # 仍然是哈希表思路。只遍历一趟原数组，每存一个数字就判断左右是否已经存在，若已存在，则值域存放当前连续的最大长度。
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mydict = {}
        res = 1
        for num in nums:
            # 若当前数字已存在，则跳过
            if num in mydict.keys(): continue
            # 先将当前数字存进哈希表
            mydict[num] = 1
            ll = num
            rr = num
            val = 1
            # 若当前数字的左边存在
            if num - 1 in mydict.keys():
                ll = num - mydict[num - 1]
                val += mydict[num - 1]
            if num + 1 in mydict.keys():
                rr = num + mydict[num + 1]
                val += mydict[num + 1]
            mydict[ll] = val
            mydict[rr] = val
            res = max(res, val)
        return res

    # 考虑负数的情况：用哈希表。超时。
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mydict = {}
        m = max(nums)
        for num in nums:
            if num not in mydict.keys():
                mydict[num] = 1
        res = 0
        for num in nums:
            cur = 1  # 记录当前数字开始，最长连续序列的长度
            while num + 1 in mydict.keys() and num + 1 <= m:
                cur += 1
                num += 1
            res = max(res, cur)
        return res

    # 不考虑负数的情况，用一个数据记录原数据即可
    def longestConsecutive3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        m = max(nums)
        temp = [0 for _ in range(m + 1)]
        for num in nums:
            if num >= 0:
                temp[num] = 1
        res = 0
        cur_size = 0
        for i in range(m + 1):
            if temp[i] != 0:
                cur_size += 1
            else:
                res = max(res, cur_size)
                cur_size = 0
        res = max(res, cur_size)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(s.longestConsecutive([0, -1]))
