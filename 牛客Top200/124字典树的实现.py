# @param operators string字符串二维数组 the ops
# @return string字符串一维数组
#
# 1.void insert(String word)：添加word，可重复添加；
# 2.void delete(String word)：删除word，如果word添加过多次，仅删除一次；
# 3.boolean search(String word)：查询word是否在字典树中出现过(完整的出现过，前缀式不算)；
# 4.int prefixNumber(String pre)：返回以字符串pre作为前缀的单词数量。
class Solution:
    def trieU(self, operators):
        # 判空
        if not operators:
            return []
        mydict = {}
        res = []
        for item in operators:
            if item[0] == "1":
                if item[1] in mydict.keys():
                    mydict[item[1]] += 1
                else:
                    mydict[item[1]] = 1
            elif item[0] == "2":
                if mydict[item[1]] > 1:
                    mydict[item[1]] -= 1
                else:
                    mydict.pop(item[1])
            elif item[0] == "3":
                if item[1] in mydict.keys():
                    res.append("YES")
                else:
                    res.append("NO")
            else:
                temp = 0
                for k, v in mydict.items():
                    if self.judge(k, item[1]): temp += v
                res.append(str(temp))
        return res

    # 判断tar是不是word的前缀
    def judge(self, word, tar):
        if not tar: return True
        if len(word) < len(tar): return False
        num = len(tar)
        return word[:num] == tar


if __name__ == '__main__':
    s = Solution()
    print(s.trieU(
        [["1", "qwer"], ["1", "qwe"], ["3", "qwer"], ["4", "q"], ["2", "qwer"], ["3", "qwer"], ["4", "q"]]))
# res = ["YES","2","NO","1"]
