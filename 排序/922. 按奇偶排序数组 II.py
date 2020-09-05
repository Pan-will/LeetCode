"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。

示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

思路：
1、遍历A，取出其中的奇数(list1)、偶数（list2）；
2、遍历A，下标为奇数时从list1中取一个元素插入；
3、下标为偶数时从list2中去一个元素插入；
4、返回A。
"""


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        list1 = []
        list2 = []
        for i in range(len(A)):
            if A[i] % 2 != 0:
                list1.append(A[i])
            else:
                list2.append(A[i])
        index1 = index2 = 0
        for i in range(len(A)):
            if i % 2 != 0:
                A[i] = list1[index1]
                index1 += 1
            else:
                A[i] = list2[index2]
                index2 += 1
        return A


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArrayByParityII([4, 2, 5, 7]))
