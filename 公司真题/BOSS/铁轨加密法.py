class Solution:
    def railEncode(self, data, n):
        if not data:
            return ""
        size = len(data)
        if size <= n:
            return data
        res = [[] for _ in range(n)]  # 模拟n条铁轨
        cur_row = 0  # 铁轨指针，指当前遍历到哪条铁轨
        down = 0  # 判断是否要反向
        for ch in data:
            res[cur_row].append(ch)  # 将当前字符放到对应轨道上
            if cur_row == 0 or cur_row == n - 1:  # 判断是否要转向：第一行或最后一行才转向
                down = 1 if not down else 0
            cur_row += 1 if down else -1  # 根据是否转向，判断铁轨指针的指向
        # 格式化输出
        ans = ""
        for item in res:
            ans += "".join(item)
        return ans


if __name__ == '__main__':
    s = Solution()
    data = "abcdefghijklmno"
    # print(data[10: 20], len(data[10:20]))
    print(s.railEncode(data, 3))
