"""
实现一个MyQueue类，该类用两个栈来实现一个队列。

示例：
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 入栈，模拟进队
        self.stackIn = []
        # 出栈，模拟出队
        self.stackOut = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stackIn.append(x)

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

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stackIn and not self.stackOut

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
