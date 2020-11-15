class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        # 交换可行的则为True
        list1 = list(word1)
        list1.sort()
        list2 = list(word2)
        list2.sort()
        if list1 == list2:
            return True
        # 变换可行的也为True
        dict1 = {}
        for ch in word1:
            if ch in dict1.keys():
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        mylist1 = sorted(dict1.items(), key=lambda x: x[1], reverse=False)
        dict2 = {}
        for ch in word2:
            if ch in dict2.keys():
                dict2[ch] += 1
            else:
                dict2[ch] = 1
        mylist2 = sorted(dict2.items(), key=lambda x: x[1], reverse=False)

        if len(mylist1) != len(mylist2):
            return False
        for i in range(len(mylist1)):
            if mylist1[i][1] != mylist2[i][1]:
                return False
            if mylist1[i][0] not in dict2.keys():
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.closeStrings(word1="cabbba", word2="aabbss"))
    print(s.closeStrings(word1="cabbba", word2="abbccc"))
    print(s.closeStrings(word1="abc", word2="bca"))
    print(s.closeStrings("uau", "ssx"))
