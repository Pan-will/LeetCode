"""
布隆过滤器
用来干啥？ 判断一个元素是否存在于一个海量的集合中！在redis中用来过滤非法请求。
的核心实现：一个超大的位数组 + n个哈希函数。
设redis中的key集合长度为n，则该过滤器应设置n个哈希函数。先遍历每一个key，用n个哈希函数得到n个哈希码，在位数组中将哈希码对应位置为1。
当新请求到来时，也分别用n个哈希函数得到n个哈希码，查询位数组，若所有位置都是1，则该请求key可能在redis中，合法请求！只要有一个位置不是1，那就拒绝该请求。
"""
import mmh3
from bitarray import bitarray

# Implement a simple bloom filter with murmurhash algorithm.
# Bloom filter is used to check wether an element exists in a collection, and it has a good performance in big data situation.
# It may has positive rate depend on hash functions and elements count.


BIT_SIZE = 5000000


class BloomFilter:

    def __init__(self):
        # Initialize bloom filter, set size and all bits to 0
        bit_array = bitarray(BIT_SIZE)
        bit_array.setall(0)

        self.bit_array = bit_array

    def add(self, url):
        # Add a url, and set points in bitarray to 1 (Points count is equal to hash funcs count.)
        # Here use 7 hash functions.
        point_list = self.get_postions(url)

        for b in point_list:
            self.bit_array[b] = 1

    def contains(self, url):
        # Check if a url is in a collection
        point_list = self.get_postions(url)

        result = True
        for b in point_list:
            result = result and self.bit_array[b]

        return result

    def get_postions(self, url):
        # Get points positions in bit vector.
        point1 = mmh3.hash(url, 41) % BIT_SIZE
        point2 = mmh3.hash(url, 42) % BIT_SIZE
        point3 = mmh3.hash(url, 43) % BIT_SIZE
        point4 = mmh3.hash(url, 44) % BIT_SIZE
        point5 = mmh3.hash(url, 45) % BIT_SIZE
        point6 = mmh3.hash(url, 46) % BIT_SIZE
        point7 = mmh3.hash(url, 47) % BIT_SIZE

        return [point1, point2, point3, point4, point5, point6, point7]


if __name__ == '__main__':
    blong = BloomFilter()
    blong.get_postions(55)
