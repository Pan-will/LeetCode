def getAns(state, yilai_dict, op, index):
    # 若是开启操作
    if op == 1:
        state[index] = 1
        yilai = yilai_dict[index]
        # 存放本次操作需要开启的所有依赖节点
        need = []
        # 参考层序遍历，用队列寻找所有依赖节点
        while yilai:
            num = len(yilai)
            for _ in range(num):
                node_index = yilai.pop()
                need.append(node_index)
                if yilai_dict[node_index]:
                    yilai += yilai_dict[node_index]

        for item in need:
            state[item] = 1
    # 若是关闭操作
    elif op == 0:
        state[index] = 0
        for key, value in yilai_dict.items():
            for node_index in value:
                if node_index == index:
                    state[key] = 0


n, q = map(int, input().split())
# 统计每个节点，以及他们所依赖的节点
yilai_dict = {}
# 记录节点
nodes = []
# 记录每个节点的当前状态
state = {}

for i in range(1, n + 1):
    nodes.append(i)
    # 初始化所有节点都是关闭状态
    state[i] = 0
    yilai = list(map(int, input().split()))
    # 节点序号为key，其依赖的节点数组为value
    yilai_dict[i] = yilai[1:]
# 返回值
# res = []
print("依赖关系：", yilai_dict)
for i in range(q):
    op, index = map(int, input().split())
    getAns(state, yilai_dict, op, index)

    # 统计当前操作后，还运行的节点数
    cur_ing = 0
    for key, value in state.items():
        if value == 1:
            cur_ing += 1
    print("第", i + 1, "次操作后各节点的状态：", state)
    print("共有", cur_ing, "个节点在运行。")

# for item in res:
#     print(item)


"""
4 3
2 2 4
2 3 4
3 1 2 4
1 2
1 1
0 4
"""