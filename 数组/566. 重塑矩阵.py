"""
给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:
输入:
nums = [[1,2], [3,4]], r = 1, c = 4
输出:
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
"""


class Solution(object):
    # 思路：将原nums中的元素都读出来，在往新list中加。
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # nums行数
        r0 = len(nums)
        # nums列数
        c0 = len(nums[0])
        # 若reshape操作不合理，返回原list
        if r0 * c0 != r * c:
            return nums
        new = []
        for i in range(r0):
            for j in range(c0):
                new.append(nums[i][j])
        ans = []
        flag = 0
        for k in range(r):
            temp = []
            for h in range(c):
                temp.append(new[flag])
                flag += 1
            ans.append(temp)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.matrixReshape([[1, 2], [3, 4]], r=1, c=4))
