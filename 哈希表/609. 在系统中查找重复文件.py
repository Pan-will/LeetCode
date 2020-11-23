"""
给定一个目录信息列表，包括目录路径，以及该目录中的所有包含内容的文件，您需要找到文件系统中的所有重复文件组的路径。一组重复的文件至少包括二个具有完全相同内容的文件。

输入列表中的单个目录信息字符串的格式如下：

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

这意味着有 n 个文件（f1.txt, f2.txt ... fn.txt 的内容分别是 f1_content, f2_content ... fn_content）在目录 root/d1/d2/.../dm 下。注意：n>=1 且 m>=0。如果 m=0，则表示该目录是根目录。

该输出是重复文件路径组的列表。对于每个组，它包含具有相同内容的文件的所有文件路径。文件路径是具有下列格式的字符串：
"directory_path/file_name.txt"

示例 1：
输入：
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
输出：
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
"""

import re
# 本题用dict做，思路很明确：用文件内容作key域，value域需要拼接，是文件全名。
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        mydict = {}
        for item in paths:
            temp = item.split()
            # 获取当前路径
            path = temp[0]
            # 获取当前路径下的所有文件
            files = temp[1:]
            # 遍历每一个文件，取文件内容作为key，往mydict里存
            for file in files:
                # 用正则表达式获取文件内容
                fileContextList = re.findall(r'[(](.*?)[)]', file)
                fileContextStr = ''.join(fileContextList)
                extraSize = len(fileContextStr) + 2
                fileName = list(file)[:-extraSize]
                if fileContextStr in mydict.keys():
                    mydict[fileContextStr].append(path + "/" + ''.join(fileName))
                else:
                    mydict[fileContextStr] = [path + "/" + ''.join(fileName)]
        res = []
        for item in mydict.values():
            if len(item) > 1:
                res.append(item)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate(
        ["root/a 1.txt(abcd) 2.txt(efsfgh)", "root/c 3.txt(abdfcd)", "root/c/d 4.txt(efggdfh)"]))
