"""
在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，
判断这个机器人在完成移动后是否在 (0, 0) 处结束。
移动顺序由字符串表示。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。
如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。
此外，假设每次移动机器人的移动幅度相同。

示例 1:
输入: "UD"
输出: true

思路：
1、设置两个计数器分别记录U和R的出现次数；
2、遍历字符串，遇到D则与U抵消，L与R抵消，最后计数器均为0则回到了原点。
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves == "":
            return True
        # 设置两个计数器
        numu = 0
        numr = 0
        # 遍历字符串，遇到D则与U抵消，L与R抵消，最后计数器均为0则回到了原点
        for i in range(len(moves)):
            if moves[i] == 'U':
                numu += 1
            elif moves[i] == 'D':
                numu -= 1
            elif moves[i] == 'R':
                numr += 1
            else:
                numr -= 1
        if numu == 0 and numr == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.judgeCircle("UD"))
