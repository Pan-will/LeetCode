"""
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。
如果不存在，对应位置输出 -1 。
 

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
"""


class Solution(object):
    # 思路：用栈。
    # 将nums2顺序入栈stack[]，当栈不空时，取待入栈元素num和栈顶元素top比较，若num>top且top在nums1中，则num即是所找的数。
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 初始化返回值
        ans = [-1]*len(nums1)
        # 用字典记录下nums1中每个元素的下标
        dict = {}
        for i, num in enumerate(nums1):
            dict[num] = i
        # 模拟栈
        stack = []
        # 遍历nums2
        for num in nums2:
            # 当栈不空，且栈顶元素小于待入栈数字
            while stack and stack[-1] < num:
                # 取栈顶元素
                top = stack.pop()
                # 若栈顶元素在nums1中，则num即为nums2右侧比top大的第一个元素，记录在ans中
                if top in dict:
                    ans[dict[top]] = num
            # 栈空则将当前数字入栈
            stack.append(num)
        return ans

    def nextGreaterElement2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            temp = nums2[index + 1:]
            # 在nums1右侧是否找到更大元素的标志
            flag = False
            for j in range(len(temp)):
                if temp[j] > nums1[i]:
                    ans.append(temp[j])
                    # 标志置真
                    flag = True
                    break
            # 没找到则返回-1
            if not flag:
                ans.append(-1)
        return ans

    def nextGreaterElement3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            temp = nums2[index + 1:]
            for j in range(len(temp)):
                if temp[j] > nums1[i]:
                    ans.append(temp[j])
                    break
            # 没找到则返回-1
            # 原来python里的else还能这么用！！
            else:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
