"""
LeetCode 设计了一款新式键盘，正在测试其可用性。
测试人员将会点击一系列键（总计 n 个），每次一个。

给你一个长度为 n 的字符串 keysPressed ，其中 keysPressed[i] 表示测试序列中第 i 个被按下的键。
releaseTimes 是一个升序排列的列表，其中 releaseTimes[i] 表示松开第 i 个键的时间。
字符串和数组的 下标都从 0 开始 。
第 0 个键在时间为 0 时被按下，接下来每个键都 恰好 在前一个键松开时被按下。

测试人员想要找出按键持续时间最长的键。
第 i 次按键的持续时间为releaseTimes[i]-releaseTimes[i-1],第0次按键的持续时间为releaseTimes[0] 。

注意，测试期间，同一个键可以在不同时刻被多次按下，而每次的持续时间都可能不同。

请返回按键 持续时间最长 的键，如果有多个这样的键，则返回 按字母顺序排列最大 的那个键。

示例 1：
输入：releaseTimes = [9,29,49,50], keysPressed = "cbcd"
输出："c"
解释：按键顺序和持续时间如下：
按下 'c' ，持续时间 9（时间 0 按下，时间 9 松开）
按下 'b' ，持续时间 29 - 9 = 20（松开上一个键的时间 9 按下，时间 29 松开）
按下 'c' ，持续时间 49 - 29 = 20（松开上一个键的时间 29 按下，时间 49 松开）
按下 'd' ，持续时间 50 - 49 = 1（松开上一个键的时间 49 按下，时间 50 松开）
按键持续时间最长的键是 'b' 和 'c'（第二次按下时），持续时间都是 20
'c' 按字母顺序排列比 'b' 大，所以答案是 'c'
"""


class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        time = []
        for i, item in enumerate(releaseTimes):
            if i == 0:
                time.append(item)
            else:
                time.append(item - releaseTimes[i - 1])
        mydict = {}
        for i in range(len(time)):
            mydict[i] = time[i]
        # 取出最长持续时间
        maxitem = max(time)
        # 存放同为最长时间的字符，最后按字典排序返回最大者
        res = []
        # 寻找keysPressed中同为最长时间的字符
        for k, v in mydict.items():
            if v == maxitem:
                res.append(keysPressed[k])
        res.sort()
        return res[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd"))
