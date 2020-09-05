"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 返回值
        ans = []
        # 去重升序
        s = sorted(set(nums))
        index = 0
        # 遍历整数1到n
        # range[start,end)：左闭右开
        for i in range(1, len(nums)+1):
            if index < len(s) and i == s[index]:
                index += 1
            # 若i不在原数组中，则添加到返回值中
            else:
                ans.append(i)
        return ans

    # 果断超时！
    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        for i in range(1, n + 1):
            if i not in nums:
                ans.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(solution.findDisappearedNumbers([1, 1]))
