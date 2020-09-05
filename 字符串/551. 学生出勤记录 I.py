"""
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:
输入: "PPALLP"
输出: True

思路：
1、统计原串中A的个数，大于1则返回False;
2、遍历原串，当遇到L时（下标为index），截取index往后的三个字符，若是LLL则返回False;
3、遍历结束，返回True。
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 原串中A的个数大于1
        if s.count('A') > 1:
            return False
        for index, ch in enumerate(s):
            # 连续出现三个L
            if ch == 'L' and s[index:index + 3] == 'LLL':
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkRecord("PPALLP"))
    print(solution.checkRecord("ALL"))
