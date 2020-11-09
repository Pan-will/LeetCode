"""
示例 4：
输入：rains = [69,0,0,0,69]
输出：[-1,69,1,1,-1]
解释：任何形如 [-1,69,x,y,-1], [-1,x,69,y,-1] 或者 [-1,x,y,69,-1] 都是可行的解，其中 1 <= x,y <= 10^9

示例 5：
输入：rains = [10,20,20]
输出：[]
解释：由于湖泊 20 会连续下 2 天的雨，所以没有没有办法阻止洪水。
"""


class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        # 先遍历一趟，有连续相等且大于0的两个元素则无法阻止洪水，返回[]
        i = 1
        while i < len(rains):
            if rains[i] == rains[i - 1] and rains[i] > 0:
                return []
            i += 1
        mydict = {}


if __name__ == '__main__':
    s = Solution()
    print(s.avoidFlood([69, 0, 0, 0, 69]))
