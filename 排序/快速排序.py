def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index + 1, high)


if __name__ == '__main__':
    # array是已知的二进制序列号数组
    array = []
    # 将二进制转成十进制在快拍
    mylist = []
    for i in array:
        mylist.append(int(i, 2))
    quick_sort(mylist, 0, len(mylist) - 1)
    for k,v in enumerate(mylist):
        mylist[k] = bin(v)[2:]
    print(mylist)

