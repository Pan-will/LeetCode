#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
class Solution:
    def LRU(self, operators, k):
        stack = []
        kv = {}
        res = []
        for op in operators:
            if op[0] == 1:
                # 缓存未满
                if len(stack) < k:
                    stack.append([op[1], op[2]])
                    kv[op[1]] = op[2]
                # 缓存已满，退出最久没访问的kv
                else:
                    # 先退出
                    k, v = stack.pop(0)
                    kv.pop(k)
                    # 存最新数据
                    stack.append([op[1], op[2]])
                    kv[op[1]] = op[2]
            elif op[0] == 2:
                if op[1] not in kv.keys():
                    res.append(-1)
                else:
                    temp = kv[op[1]]
                    res.append(temp)
                    stack.remove([op[1], temp])
                    stack.append([op[1], temp])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3))
