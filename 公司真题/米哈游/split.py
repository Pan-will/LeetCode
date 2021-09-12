# -*- coding:utf-8 -*-

# re模块,实现正则匹配

import re

str_test = 'abcdefgHABC123456中华民族'

# 把正则表达式编译成对象,如果经常使用该对象,此种方式可提高一定效率
hanzi_regex = re.compile(r'[\u4E00-\u9FA5]')
print('输入字符串:', str_test)
# findall获取字符串中所有匹配的字符
hanzi_list = hanzi_regex.findall(str_test)

print('包含的汉字:', hanzi_list)
