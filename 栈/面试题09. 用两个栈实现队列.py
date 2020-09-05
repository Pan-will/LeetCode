"""
用两个栈实现一个队列。
队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead：
分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
"""


class CQueue(object):

    def __init__(self):
        # 入栈，模拟进队
        self.stackIn = []
        # 出栈，模拟出队
        self.stackOut = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stackIn.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if CQueue.empty():
            return -1
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
            return self.stackOut.pop()
        else:
            return self.stackOut.pop()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stackIn and not self.stackOut

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
