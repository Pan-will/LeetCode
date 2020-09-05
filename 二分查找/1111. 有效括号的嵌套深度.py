"""
示例 1：
输入：seq = "(()())"
输出：[0,1,1,1,1,0]

示例 2：
输入：seq = "()(())()"
输出：[0,0,0,1,1,0,1,1]
解释：本示例答案不唯一。
按此输出 A = "()()", B = "()()", max(depth(A), depth(B)) = 1，它们的深度最小。
像 [1,1,1,0,0,1,1,1]，也是正确结果，其中 A = "()()()", B = "()", max(depth(A), depth(B)) = 1 。
"""


class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        res = []
        if not seq:
            return res
        depth, max_depth = 0, 0
        for ch in seq:
            if ch == "(":
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        a_depth = 0
        mid = 1 + (max_depth-1)//2
        for ch in seq:
            if ch == "(":
                if a_depth < mid:
                    res.append(0)
                    a_depth += 1
                else:
                    res.append(1)
            else:
                if a_depth > 0:
                    res.append(0)
                    a_depth -= 1
                else:
                    res.append(1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDepthAfterSplit(seq="(()())"))
