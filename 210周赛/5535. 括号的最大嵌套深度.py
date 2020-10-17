class Solution(object):
    # 题设已表明：给定的s一定是有效的，所以不用进行合法性判断。
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 特判空字符串
        if s == "":
            return 0
        # 特判单字符
        if len(s) == 1 and s != "(" and s != ")":
            return 0
        # 模拟栈
        stack = []
        # 栈的当前深度
        depth = 0
        # 栈的最大深度，即返回值
        maxDep = 0
        # 遍历字符串
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(ch)
            if ch == ")":
                stack.pop()
            depth = len(stack)
            maxDep = max(depth, maxDep)
        return maxDep


if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth(s="(1+(2*3)+((8)/4))+1"))
