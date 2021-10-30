# 返回list1中有而list2中没有的元素
def diff_list(list1, list2):
    return list(set(list1) - set(list2))


dict1 = [
    {
        '扫描':
            {
                'time_start': '2021-10-12 15:11:15',
                'time_end': '2021-10-12 17:01:05',
                'count': 4,
                'domain_list': ['www.hqsec.cn', 'www.baidu.cn']
            }
    },
    {
        'sql':
            {
                'time_start': '2021-10-09 00:03:03',
                'time_end': '2021-10-23 17:01:05',
                'count': 4,
                'domain_list': ['www.hqsec.cn', 'www.baidu.cn']
            }
    },
    {
        'xss':
            {
                'time_start': '2021-10-08 00:03:03',
                'time_end': '2021-10-28 17:01:05',
                'count': 3,
                'domain_list': ['www.baidu.cn']
            }
    },
]

dict2 = [
    {
        'sql':
            {
                'time_start': '2021-10-09 00:03:03',
                'time_end': '2021-10-23 17:01:05',
                'count': 11,
                'domain_list': ['www.shouguan.cn', 'aaa.shouguan.cn']
            }
    },
    {
        '扫描':
            {
                'time_start': '2021-10-09 00:03:03',
                'time_end': '2021-10-23 17:01:05',
                'count': 30,
                'domain_list': ['www.shouguan.cn', 'aaa.shouguan.cn']
            }
    },
    {
        'dict2_unique':
            {
                'time_start': '2021-10-09 00:03:03',
                'time_end': '2021-10-23 17:01:05',
                'count': 30,
                'domain_list': ['www.shouguan.cn', 'aaa.shouguan.cn']
            }
    }
]

res = {}

# 构造两个列表分别存放dict1和dict2的key，方便判断是否存在独有元素
# res存放dict1和dict2的并集
temp1 = []
# 暴力，用空间换时间吧
new_dict1 = {}
for item in dict1:
    for k, v in item.items():
        new_dict1[k] = v
        temp1.append(k)
        res[k] = v
# print(new_dict1)
temp2 = []
new_dict2 = {}
for item in dict2:
    for k, v in item.items():
        new_dict2[k] = v
        temp2.append(k)
        if k not in res.keys():
            res[k] = v

"""
time_start = dic1中的sql['time_start'], 
time_end = dic1中的sql['time_end'], 
count = dic1中的sql['count'], 
current_domain = dic1中的'sql'['domain_list'], 

other_attack_count = dic2中的'sql'['count'], 
other_domain = dic2中的'sql'['domain_list']
"""
for key, value in res.items():
    # 移除多余字段，添加新字段
    value.pop('domain_list')
    value['current_domain'] = []
    value['other_attack_count'] = 0
    value['other_domain'] = []

# 条件1：若dict1中有xss字典，但dict2中没有xss字典，此时all_data中：other_attack_count=0，other_domain =[]；
if 'xss' in temp1 and 'xss' not in temp2:
    for key, value in res.items():
        for k1, v1 in value.items():
            if k1 == 'time_start':
                v1 = new_dict1[key][k1]
            elif k1 == 'time_end':
                v1 = new_dict1[key][k1]
            elif k1 == 'count':
                v1 = new_dict1[key][k1]
            elif k1 == 'current_domain':
                v1 = new_dict1[key]['domain_list']
            elif k1 == 'other_attack_count':
                v1 = 0
            elif k1 == 'other_domain':
                v1 = []

const = {
    "time_start": 0,
    "time_end": 0,
    "count": 0,
    "other_attack_count": 0,
    "current_domain": [],
    "other_domain": []
}
# 条件2：dict2中拥有dict1中没有的元素，此时all_data中：time_start, time_end, count, current_domain均为0或None。
if diff_list(temp2, temp1):
    for key, val in res.items():
        val = const

all_data = {}
all_data['64'] = res
print(all_data)
