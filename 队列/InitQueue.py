# 定义队列类
class MyQueue(object):
    # 队列初始化
    def __init__(self, size):
        self.size = size  # 定义队列容量
        self.queue = []  # 存储队列

    # 入队
    def inQueue(self, n):
        if self.isFull():
            return -1
        self.queue.append(n)  # 列表末尾添加新的对象

    # 删除某元素
    def delete(self, n):
        element = self.queue[n]
        self.queue.remove(element)

    # 插入某元素 n代表列表当前的第n位元素 m代表传入的值
    def inPut(self, n, m):
        self.queue[n] = m

    # 获取当前队列中的元素个数，即队列长度
    def getSize(self):
        return len(self.queue)

    # 判断是否为空
    def isEmpty(self):
        return len(self.queue) == 0

    # 判断队列是否满
    def isFull(self):
        return len(self.queue) == self.size


if __name__ == '__main__':
    # 定义一个大小为5的队列
    queue = MyQueue(5)
    for i in range(8):
        if not queue.isFull():
            queue.inQueue(i)
        else:
            queue.inQueue(i)
        print(queue)
