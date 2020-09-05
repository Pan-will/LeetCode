# 定义链表节点：数据域、指针域
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 定义单链表：头指针、尾指针、链表长度
class linkOne(object):
    def __init__(self):
        # 头指针
        self.head = None
        # 尾指针
        self.tail = None
        # 元素个数，即链表长度
        self.count = 0

    def isEmpty(self):
        # return self.count == 0
        if self.count == 0:
            return True
        else:
            return False

    def size(self):
        return self.count

    # 添加节点到尾部：尾插法
    def addElementToTail(self, data):
        # 若尾指针不为空
        if (self.tail != None):
            # 新建一个节点并存入数据
            temp = Node(data, None)
            # 添加节点
            self.tail.next = temp
            # 尾指针后移
            self.tail = temp
            # 链表长度加1
            self.count += 1
        # 尾指针为空
        else:
            self.head = self.tail = Node(data, None)
            self.count += 1

    # 删除节点
    def DeleteElementFromTail(self):
        # 链表为空：头、尾指针都指向首节点
        if (self.head == self.tail):
            self.count = 0
            self.head = self.tail = None
        # 链表不为空
        else:
            temp = self.tail
            t = self.head
            while (t.next != self.tail):
                t = t.next
            self.tail = t
            self.count -= 1
            del temp
        # return temp.data


lk = linkOne()
lk.addElementToTail(10)
lk.addElementToTail(20)
lk.addElementToTail(30)
lk.addElementToTail(40)

print(lk.head.data, lk.head.next.data)
pre = None
while lk.head:
    temp = lk.head.next
    lk.head.next = pre
    pre = lk.head
    lk.head = temp
print(pre.data)

# print(lk.size())
# print(lk.head.data, lk.head.next.data, lk.head.next.next.data)
# k = 2
# flag = lk.head
# while k > 0:
#     lk.head = lk.head.next
#     k -= 1
# low = flag
# print(low.data, lk.head.data, lk.tail.data)
# while lk.head != lk.tail:
#     lk.head = lk.head.next
#     low = low.next
# print("倒数第k个元素是：", low.next.data)
