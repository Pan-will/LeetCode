"""
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in nums:
            length = len(res)
            for j in range(length):
                res.append(res[j] + [i])
            res.append([i])
        res.append([])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3,4]))
