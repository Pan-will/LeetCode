class DoubleLink(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = DoubleLink()
        self.tail = DoubleLink()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
        self.capacity = capacity
        self.mydict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mydict.keys():
            return -1
        node = self.mydict[key]
        self.MoveToHead(node)
        return node.val

    def MoveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def addToHead(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.mydict.keys():
            node = DoubleLink(key, value)
            self.mydict[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                delNode = self.delTail()
                self.mydict.pop(delNode.key)
                self.removeNode(delNode)
                self.size -= 1
        else:
            node = self.mydict[key]
            node.val = value
            self.MoveToHead(node)

    def delTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node
