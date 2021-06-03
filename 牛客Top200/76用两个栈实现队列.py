# -*- coding:utf-8 -*-
class Solution:
    # 初始化
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 入栈，模拟进队
        self.stackIn = []
        # 出栈，模拟出队
        self.stackOut = []

    def push(self, node):
        self.stackIn.append(node)

    def pop(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
            return self.stackOut.pop()
        else:
            return self.stackOut.pop()
