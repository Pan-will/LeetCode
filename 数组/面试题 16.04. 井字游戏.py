"""
设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。

以下是井字游戏的规则：

玩家轮流将字符放入空位（" "）中。
第一个玩家总是放字符"O"，且第二个玩家总是放字符"X"。
"X"和"O"只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。
如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。

示例 1：

输入： board = ["O X"," XO","X O"]
输出： "X"
"""


class Solution:
    def tictactoe(self, board):
        """
        :type board: List[str]
        :rtype: str
        """
        N = len(board)
        x = ['X'] * N
        o = ['O'] * N
        if 'X' * N in board:
            return 'X'
        if 'O' * N in board:
            return 'O'

        def judgement(arr):
            if arr == x:
                return True
            if arr == o:
                return True
            return False

        for i in range(N):
            # temp = [j[i] for j in board]
            temp = board[i]
            print("第", i + 1, "行：", temp)
            # 判断行是否胡牌
            if judgement(temp):
                return temp[0]

        temp1 = []
        temp2 = []
        for i in range(N):
            # 正对角线
            temp1.append(board[i][i])
            # 副对角线
            temp2.append(board[i][N - 1 - i])
        if judgement(temp1):
            return temp1[0]
        if judgement(temp2):
            return temp2[0]
        # 到此还未分胜负，则判断是否有空位，继续下棋
        for i in board:
            if ' ' in i:
                return 'Pending'
        # 未分胜负、无空位，则平局
        return 'Draw'


if __name__ == '__main__':
    solution = Solution()
    print(solution.tictactoe(board=["O X", " XO", "X O"]))
