# 定义链表节点类
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value  # 节点元素
        self.next = next  # 指针


# 单链表类
class LinkedList(object):
    def __init__(self):
        self.head = Node()  # 创建头结点
        self.length = 0  # 初始化链表长度

    def __len__(self):
        return self.length

    def __iter__(self):  # 遍历列表节点
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        curnode = self.head.next
        while curnode.next != None:
            yield curnode
            curnode = curnode.next
        if curnode.next == None:
            yield curnode

    def head_insert(self, value):  # 链表头部插入
        node = Node(value)
        if self.head.next == None:
            self.head.next = node
            node.next = None
        else:
            # 插入元素指针域指向原head元素
            tmp_head = self.head.next  # 原头指针节点存储到tmp_head
            self.head.next = node  # 新head指针指向node
            node.next = tmp_head  # 新插入节点指向原头指针节点
        self.length += 1

    def head_del(self):  # 删除头结点,返回头结点的值
        if self.head.next == None:
            return False
        else:
            # 头指针指针域指向自己
            self.head = self.head.next
            self.length -= 1
            return self.head.value

    def append(self, value):  # 链表尾部添加结点
        # 创建新插入的结点对象
        node = Node(value)
        if self.length == 0:
            self.head.next = node  # 只有一个节点，指针指向自己
        else:
            curnode = self.head.next  # 变量curnode存放指针
            while curnode.next != None:
                curnode = curnode.next
            curnode.next = node  # 当为最后一个节点时，指针指向新插入节点
        self.length += 1

    # 这里的insert是指定值后面插入不是指定位置
    def insert(self, index, value):
        node = Node(value)
        if self.length == 0:
            self.head.next = node
            self.length += 1
        else:
            for nd in self.iter_node():
                if nd.value == index:  # 如果nd节点值等于index，则插入到nd后
                    tmp_node = nd.next  # 将nd的指针存放到中间变量
                    nd.next = node  # nd节点指向插入节点
                    node.next = tmp_node  # 插入节点指向原nd.next节点
                    self.length += 1
                    return True
            return False

    def replace(self, old_value, new_value):
        index = 0
        if self.length == 0:
            return False
        else:
            for node in self.iter_node():
                if node == old_value:
                    node.value = new_value
                    index += 1
        if index != 0:
            return index  # 替换节点数量(存在节点值相同情况)
        else:
            return False  # 替换失败，未找到替换值

    def delete_node(self, value):
        Flag = False
        if self.length == 0:
            return False
        else:
            previous_node = self.head  # 初始化前置节点为头结点
            for node in self.iter_node():
                if node.value == value:
                    previous_node.next = node.next  # 前置节点指针指向当前节点的后继节点
                    del node
                    self.length -= 1
                    Flag = True
                else:
                    previous_node = node  # 更新前置节点的值
            return Flag


# 测试
l = LinkedList()
l.append(1)
l.append(2)
l.append(7)
l.append(5)
l.append(6)
l.append(7)
l.head_insert(3)
print("当前链表长度：%s" % l.length)
# print("删除头结点为：%d"% l.head_del())
print("当前链表长度：%s" % l.length)
i = 1
# l.delete_node(7)
for node in l:
    print("第%d个链表节点的值: %d" % (i, node))
    i += 1
