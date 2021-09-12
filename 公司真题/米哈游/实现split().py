#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 截取字符串
# @param original string字符串
# @param count int整型
# @return string字符串
#

"""
思路：
1、original字符串挨个遍历，用bit array存放，字母用1表示，非字母用2表示；
2、遍历bit array，并累加元素sum；
3、若sum==count，刚好相等，则取当前bit array的下标i，并返回original[:i];
4、若sum>count，向下取整，去当前bit array的下标i，并返回original[:i]。
"""

import re
class Solution:
    def cutString(self, original, count):
        # write code here
        # 判空
        if not original or count < 1:
            return ""
        bit_arr = []
        hanzi_regex = re.compile(r'[\u4E00-\u9FA5]')
        hanzi_list = hanzi_regex.findall(original)
        print(hanzi_list)
        for ch in original:
            if ch in hanzi_list:
                bit_arr.append(2)
            else:
                bit_arr.append(1)
        print("bit array is: ", bit_arr)
        temp = 0
        i = 0
        while temp < count and i < len(bit_arr):
            temp += bit_arr[i]
            i += 1
        if temp == count:
            return original[:i]
        if temp > count:
            return original[:i - 1]


if __name__ == '__main__':
    s = Solution()
    ori = "sd求一个fon,am,a"
    print(s.cutString(ori, 5))
