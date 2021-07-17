"""
示例：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
"""


class Solution(object):
    # 双指针
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # 特判:若两个都是空，返回True
        if not pushed and not popped:
            return True
        # 特判：二者长度不同，返回False
        if len(pushed) != len(popped):
            return False

        # 模拟栈
        stack = []
        # 设置双指针，分别遍历pushed和popped
        i, j = 0, 0
        while j < len(popped) and i <= len(pushed):
            while stack and stack[-1] == popped[j]:
                stack.pop(-1)
                j += 1
            if i < len(pushed):
                stack.append(pushed[i])
            i += 1
        if j == len(popped) and i == len(pushed)+1:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
    # print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
