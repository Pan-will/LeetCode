"""
给你一个长度为 n 的字符串数组 names 。
你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，
系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。
返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。

示例 1：
输入：names = ["pes","fifa","gta","pes(2019)"]
输出：["pes","fifa","gta","pes(2019)"]
解释：文件系统将会这样创建文件名：
"pes" --> 之前未分配，仍为 "pes"
"fifa" --> 之前未分配，仍为 "fifa"
"gta" --> 之前未分配，仍为 "gta"
"pes(2019)" --> 之前未分配，仍为 "pes(2019)"

示例 2：
输入：names = ["gta","gta(1)","gta","avalon"]
输出：["gta","gta(1)","gta(2)","avalon"]
解释：文件系统将会这样创建文件名：
"gta" --> 之前未分配，仍为 "gta"
"gta(1)" --> 之前未分配，仍为 "gta(1)"
"gta" --> 文件名被占用，系统为该名称添加后缀 (k)，由于 "gta(1)" 也被占用，所以 k = 2 。实际创建的文件名为 "gta(2)" 。
"avalon" --> 之前未分配，仍为 "avalon"
"""


class Solution(object):
    # python3
    def getFolderNames(self, names):
        mydict, res = {}, []
        for name in names:
            temp = name
            while temp in mydict:
                temp = f'{name}({mydict[name]})'
                mydict[name] += 1
            mydict[temp] = 1
            res.append(temp)
        return res

    def getFolderNames2(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        mydict = {}
        res = []
        for item in names:
            if item in mydict.keys():
                mydict[item] += 1
                newName = item + "(" + str(mydict[item]) + ")"
                while newName in mydict.keys():
                    mydict[item] += 1
                    newName = item + "(" + str(mydict[item]) + ")"
                res.append(newName)
                mydict[newName] = 0
            else:
                mydict[item] = 0
                res.append(item)
        return res


if __name__ == '__main__':
    s = Solution()
    # ["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]
    print(s.getFolderNames(["wano", "wano", "wano", "wano"]))
