"""
给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

提示：
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中


思路：
1、设置res=[]，extra[]；
2、遍历arr2，统计arr1中arr2[i]的个数num；
3、在res中追加num个arr2[i]；
4、遍历arr1，将没出现在arr2中的元素添加到extra中；
5、将extra升序排列，返回res+extra。
"""


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        extra = []
        # 遍历arr2，统计arr1中arr2[i]的个数num,在res中追加num个arr2[i]；
        for ch in arr2:
            num = arr1.count(ch)
            res += [ch] * num
        # 遍历arr1，将没出现在arr2中的元素添加到extra中
        for ch in arr1:
            if ch not in arr2:
                extra.append(ch)
        # 将extra升序排列
        extra.sort()
        return res + extra


if __name__ == '__main__':
    solution = Solution()
    print(solution.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
