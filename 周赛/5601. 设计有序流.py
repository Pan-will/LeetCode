"""
有 n 个 (id, value) 对，其中 id 是 1 到 n 之间的一个整数，value 是一个字符串。不存在 id 相同的两个 (id, value) 对。

设计一个流，以 任意 顺序获取 n 个 (id, value) 对，并在多次调用时 按 id 递增的顺序 返回一些值。

实现 OrderedStream 类：

OrderedStream(int n) 构造一个能接收 n 个值的流，并将当前指针 ptr 设为 1 。
String[] insert(int id, String value) 向流中存储新的 (id, value) 对。存储后：
如果流存储有 id = ptr 的 (id, value) 对，则找出从 id = ptr 开始的 最长 id 连续递增序列 ，并 按顺序 返回与这些 id 关联的值的列表。然后，将 ptr 更新为最后那个  id + 1 。
否则，返回一个空列表。
"""


class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ptr = n
        self.mydict = {}

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        self.mydict[id] = [value]
        # 按id升序排
        mylist = sorted(self.mydict.items(), key=lambda x: x[0], reverse=False)
        # print(mylist)
        if id == self.ptr:
            # 找出从 id = ptr 开始的 最长 id 连续递增序列
            tarlist = mylist[mylist.index((id, [value])):]
            print(tarlist)


obj = OrderedStream(5)
param_1 = obj.insert(3, "ccccc")
p2 = obj.insert(1, "aaaaa")
p3 = obj.insert(2, "bbbbb")
p4 = obj.insert(5, "eeeee")
p5 = obj.insert(4, "ddddd")
