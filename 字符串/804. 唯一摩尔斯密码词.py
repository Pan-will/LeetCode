"""
给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。
例如，"cab" 可以写成 "-.-..--..."，(即 "-.-." + "-..." + ".-"字符串的结合)。
返回我们可以获得所有词不同单词翻译的数量。

例如:
输入: words = ["gin", "zen", "gig", "msg"]
输出: 2
解释:
各单词翻译如下:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

共有 2 种不同翻译, "--...-." 和 "--...--.".

26个字母的摩斯码：
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

思路：
逐个翻译每个单词的摩斯码，若result[]中不存在相投的摩斯码，则存入；否则翻一下一个单词；
返回result[]的有效长度；
"""


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mosiPsw = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        # 存放各单词的摩斯码，不超过100个单词
        result = [""]*100
        # result的下标：result的有效长度
        sub = 0
        # 遍历words
        for i in range(len(words)):
            # 重置摩斯码
            res = ""
            # 遍历单词的字符
            for index, ch in enumerate(words[i]):
                res += mosiPsw[ord(ch) - ord('a')]
            # print(words[i], res)
            # 将翻译的单词的摩斯码存到list中
            if res not in result:
                result[sub] = res
                # 下标加1
                sub += 1
            else:
                continue
        return sub


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
