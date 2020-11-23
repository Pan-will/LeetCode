"""
请你设计一个迭代器类，包括以下内容：

一个构造函数，输入参数包括：一个 有序且字符唯一 的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLength 。
函数 next() ，按 字典序 返回长度为 combinationLength 的下一个字母组合。
函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 True；否则，返回 False。

示例：
CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 iterator

iterator.next(); // 返回 "ab"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "ac"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "bc"
iterator.hasNext(); // 返回 false
"""


class CombinationIterator(object):
    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        # 按字典序存放长为combinationLength的所有所有字符串
        self.res = []
        string = list(characters)
        string.sort()
        n = len(string)
        visit = [0 for _ in range(n)]
        self.dfs(string, visit, n, combinationLength, 0, [])

    def dfs(self, string, visit, n, k, cur, temp):
        if len(temp) == k:
            self.res.append("".join(temp))
            return
        for i in range(cur, n):
            if not visit[i]:
                # 长度超范围，结束递归
                if len(temp) > n:
                    break
                visit[i] = 1
                self.dfs(string, visit, n, k, i + 1, temp+[string[i]])
                visit[i] = 0

    def next(self):
        """
        :rtype: str
        """
        return self.res.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.res else False


if __name__ == '__main__':
    obj = CombinationIterator("abc", 2)
    print(obj.res)
    p1 = obj.next()
    p2 = obj.hasNext()
    p3 = obj.next()
    p4 = obj.hasNext()
    p5 = obj.next()
    p6 = obj.hasNext()
    print(p1, p2, p3, p4, p5, p6)
