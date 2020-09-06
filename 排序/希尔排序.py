"""
步长序列：一般取{5，3，1}
给定数组划分时，从当前的下一个元素开始取。
"""


class Solution():
    def shell_sort(self, nums):
        # 取原序列的长度
        sizeNums = len(nums)
        # 步长
        stepList = [5, 3, 1] if sizeNums > 5 else [3, 1]

        for step in stepList:
            # 存放按步长截取过的序列
            temp = []
            for i in range(step):
                item = nums[i:sizeNums:step]
                # 内部调用插入排序
                item.sort()
                temp.append(item)
            nums = []
            index = step
            while index > 0 or temp[0]:
                for j in temp:
                    if j:
                        nums.append(j.pop(0))
                index -= 1
            print("步长为", step, "时，此趟排序结果为：", nums)
        return nums

    def test(self, nums):
        print(nums.pop(0))
        print(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.shell_sort([46, 8, 36, 50, 6, 24, 18, 78, 12, 10]))
    # print(s.test([46, 8, 36, 50, 6, 24, 18, 78, 12, 10]))
