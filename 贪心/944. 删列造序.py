"""
给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。

你需要选出一组要删掉的列 D，对 A 执行删除操作，使 A 中剩余的每一列都是 非降序 排列的，然后请你返回 D.length 的最小可能值。

删除 操作的定义是：选出一组要删掉的列，删去 A 中对应列中的所有字符，形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。（可以参见 删除操作范例）

 

示例 1：

输入：["cba", "daf", "ghi"]
输出：1
解释：
当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。
若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。
"""


class Solution(object):
    """
    思路：遍历A的每一列，用ans记录需要无序列的数量——即返回值。若当前列无序，则ans加1。
        本题思路很简单，关键在于python中内置函数的应用：zip函数和any函数是屠戮本题的神器。
    """

    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        for cl in zip(*A):
            if any(cl[i] < cl[i - 1] for i in range(1, len(cl))):
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minDeletionSize(["cba", "daf", "ghi"]))
