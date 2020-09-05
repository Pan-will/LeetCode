"""
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
注意：请不要在超过该数组长度的位置写入元素。
要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

示例 1：
输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

思路：
果然做题最难得还是读懂题意：遍历arr，遇到一个0则复制一个，最后arr长度不变；
所以：
    遍历arr，在下标为i处遇到0则insert(i,0)，并将最后一个元素pop掉，以保证arr长度不变;
"""


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1

if __name__ == '__main__':
    solution = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicateZeros2(arr)
    print(arr)
