"""
设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。
如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
实现 MagicDictionary 类：
MagicDictionary() 初始化对象
void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，
使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。
 

示例：
输入
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
输出
[null, null, false, true, false, false]

解释
MagicDictionary magicDictionary = new MagicDictionary(); //实例化对象
magicDictionary.buildDict(["hello", "leetcode"]); //构建字典
magicDictionary.search("hello"); // 返回 False
magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
magicDictionary.search("hell"); // 返回 False
magicDictionary.search("leetcoded"); // 返回 False
"""


class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mydict = {}

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            self.mydict[word] = len(word)

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        # 特判：没有相同长度的单词，肯定为False
        if len(searchWord) not in self.mydict.values():
            return False
        # 长度相同，但单词不同，且不同字符只有一个，才能返回True，否则返回False
        for word, wordSize in self.mydict.items():
            if len(searchWord) == wordSize and searchWord != word and self.canTrans(searchWord, word, wordSize):
                return True
        return False

    def canTrans(self, searchWord, word, wordSize):
        flag = 0
        for i in range(wordSize):
            if searchWord[i] != word[i]:
                flag += 1
        return flag == 1


if __name__ == '__main__':
    my = MagicDictionary()
    my.buildDict(["hello", "leetcode"])
    print(my.search("hhllo"))
