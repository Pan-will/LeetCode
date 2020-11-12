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
        # 原数组按奇偶数排个序，偶数在前，奇数在后
        A.sort(key=lambda x: x % 2 == 0, reverse=True)
        print("偶数在前，奇数在后：", A)
        n = len(A)
        if n < 3:
            return A
        if n % 2:
            i, j = 1, n - 1
        else:
            i, j = 1, n - 2
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 2
            j -= 2
        return A

    # 先将原数组中的奇偶数分开；
    # 再次遍历原数组，按照下标的奇偶分别放置奇偶数。
    def sortArrayByParityII2(self, A):
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
    print(solution.sortArrayByParityII([4, 2,5,7]))
