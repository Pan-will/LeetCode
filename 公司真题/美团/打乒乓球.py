def help(chars, mei, tuan):
    flag = 0
    for i in range(len(chars)):
        if abs(mei - tuan) > 1:
            return
        if not flag:
            if chars[i] == '1':
                mei += 1
            else:
                tuan += 1
            flag = 1
        else:
            if chars[i] == '1':
                tuan += 1
            else:
                mei += 1
            flag = 0
    return mei, tuan


def solve(s, mei, tuan):
    flag = 0  # 0表示当前为小美计分，1表示为小团计分
    index = 0
    for i in range(len(s)):
        # 谁先11分谁赢
        if mei == 11 or tuan == 11:
            return mei, tuan
        if mei == 10 and tuan == 10:
            return help(s[i:], mei, tuan)
        else:
            if index == 2:
                flag = 1 if not flag else 0
                index = 0
            if not flag and index < 2:
                if s[i] == '1':
                    mei += 1
                else:
                    tuan += 1
                index += 1
            elif flag and index < 2:
                if s[i] == '1':
                    tuan += 1
                else:
                    mei += 1
                index += 1


if __name__ == '__main__':
    s = input()
    mei, tuan = solve(s, 0, 0)
    print("%d:%d" % (mei, tuan))
"""
1111111111111111111110
"""
