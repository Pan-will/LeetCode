"""
一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。
作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。
当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。
给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。
其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。
接下来会给出一组访问次数和域名组合的列表cpdomains 。
要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。

示例 1:
输入:
["9001 discuss.leetcode.com"]
输出:
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
说明:
例子中仅包含一个网站域名："discuss.leetcode.com"。按照前文假设，子域名"leetcode.com"和"com"都会被访问，所以它们都被访问了9001次。

示例 2
输入:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
输出:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]


思路：
1、用空格截cpdomains[i]，得到访问次数num和最低级域名IP；
2、用‘.’截IP得到words，用domain[]统计顶级域名(即words[-1])和最低级域名(即IP)；
3、若len(words) == 3说明要统计二级域名(即words[1]+words[2])；
4、遍历domain[]，用字典my_dict{}统计各域名的访问次数；
5、cpdomains[]遍历统计完后将字典按规定格式转成list[str]返回。

"""


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # 返回值
        ans = []
        # 用字典统计各级域名及其访问次数
        my_dict = {}
        for i in range(len(cpdomains)):
            # 先用空格截取
            li = cpdomains[i].split()
            # 空格截取后第一部分是访问次数
            num = int(li[0])
            # 第二部分是最低一级域名
            ip = li[1]
            # 将最低一级域名用‘.’截取
            words = ip.split('.')
            # 存放各级有效域名
            domain = []
            # 统计顶级域名
            domain.append(words[-1])
            # 统计三级域名
            domain.append(ip)
            # 若最低是三级域名，则需统计二级域名
            if len(words) == 3:
                domain.append(words[1] + "." + words[2])
            # 遍历并统计各域名的访问次数
            for j in domain:
                if j not in my_dict:
                    my_dict[j] = num
                else:
                    my_dict[j] += num
        # 将字典按规定转成List[str]
        for key, value in my_dict.items():
            ans.append(str(value) + " " + key)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
    # print(solution.subdomainVisits(["9001 discuss.leetcode.com"]))