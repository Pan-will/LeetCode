"""
给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
请你返回排序后的数组。

示例 1：
输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]

思路：
sorted 和 sort函数的不同：

sorted排序会保留原list；而sort函数是在原址上排序，不会保留原迭代对象；

因此sorted 用于对可迭代对象进行排序（可迭代对象包括列表、字典、set、甚至是字符串）。

对于字符串、字典这类不可修改类型没有sort方法。

实例

sorted(arr, cmp=None, key=lambda num: (bin(num)[2:].count('1'), num), reverse=False)

和

sort(key, reverse=False)

参数列表：

arr是待排序的list；

cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。

key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。上例中有两个排序依据：首先是arr中各元素取二进制，其中‘1’字符的个数，其次是元素本身的数值大小——即将数组中的元素按照其二进制表示中数字 1 的数目升序排序。如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列；

reverse是排序规则，默认false（升序排列），true（升序排列）。
"""


class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort(key=lambda num: (bin(num)[2:].count('1'), num), reverse=False)
        return arr

    def sortByBits2(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda num: (bin(num)[2:].count('1'), num), reverse=False)


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortByBits(arr=[0, 1, 7, 8, 2, 3, 4, 5, 6]))
