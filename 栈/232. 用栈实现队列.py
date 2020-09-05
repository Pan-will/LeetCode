"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
"""


# 思路：
# 用两个栈：stackIn[] 和 stackOut[]分别模拟入队和出队；
# 注意：
# 出队时，只有当stackOut为空时才能将stackIn的元素入栈stackOut，且必须将stackIn的元素一次性全部转移到stackOut中，再出队。
# 进队时：只有当待入队元素全部进入stackIn后才能转移到stackOut，从而出队，且入队前若stackIn不为空则需等待。
class MyQueue(object):
    # 初始化
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 入栈，模拟进队
        self.stackIn = []
        # 出栈，模拟出队
        self.stackOut = []

    # 进队，本题似乎不用考虑stackIn不为空的情况，进队时默认stackIn为空
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stackIn.append(x)

    # 出队
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
            return self.stackOut.pop()
        else:
            return self.stackOut.pop()

    # 取队首元素
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
            return self.stackOut[-1]
        else:
            return self.stackOut[-1]

    # 队列判空：只有当stackIn和stackOut均为空时，队列为空。
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stackIn and not self.stackOut


# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)

    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.peek()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)

